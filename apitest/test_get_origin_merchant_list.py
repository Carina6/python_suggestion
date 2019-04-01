#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations

import pytest

from model.stone_commission.constants import MerchantType
from model.stone_commission.models import MerchantMessage
from tests.retail_loan.commission.merchant.validator import validate_origin_merchant
from xutils.verifier import Verifier
from .api import API

filter2field = [('merchantId', 'shop_no'), ('merchantName', 'shop_name'), ('merchantAddress', 'address'),
                ('merchantContactName', 'lp_name'), ('merchantContactPhone', 'mobile_no'), ('shopId', 'store_no'),
                ('shopName', 'store_name'), ('shopAddress', 'store_address')]


@pytest.mark.usefixtures('set_up_merchant_message')
def test_get_origin_merchant_list(admin_http_client, commission_db):
    res = admin_http_client.get(url=API.GET_ORIGIN_MERCHANT_LIST)
    Verifier.verify_true(res['success'])

    merchant_message_list = commission_db.query(MerchantMessage).all()
    Verifier.verify_equals(len(res['data']), len(merchant_message_list))

    for i in range(len(merchant_message_list)):
        validate_origin_merchant(res['data'][i], merchant_message_list[i])


@pytest.mark.usefixtures('set_up_merchant_message')
@pytest.mark.parametrize('merchant_type', MerchantType.get_types())
def test_get_origin_merchant_list_with_merchant_type(admin_http_client, commission_db, merchant_type):
    res = admin_http_client.get(url=API.GET_ORIGIN_MERCHANT_LIST, params=dict(merchantType=merchant_type))
    Verifier.verify_true(res['success'])

    merchant_message_list = commission_db.query(MerchantMessage).filter(
        MerchantMessage.shop_flag_g == merchant_type).all()
    Verifier.verify_equals(len(res['data']), len(merchant_message_list))

    for i in range(len(merchant_message_list)):
        validate_origin_merchant(res['data'][i], merchant_message_list[i])


@pytest.mark.parametrize('filters, field', filter2field)
def test_get_origin_merchant_list_with_single_filter(admin_http_client, commission_db, set_up_merchant_message, filters,
                                               field):
    params = {
        filters: getattr(set_up_merchant_message[0], field)
    }
    res = admin_http_client.get(url=API.GET_ORIGIN_MERCHANT_LIST, params=params)
    Verifier.verify_true(res['success'])

    merchant_message_list = commission_db.query(MerchantMessage).filter(
        getattr(MerchantMessage, field) == params[filters]).all()
    Verifier.verify_equals(len(res['data']), len(merchant_message_list))

    for i in range(len(merchant_message_list)):
        validate_origin_merchant(res['data'][i], merchant_message_list[i])


def get_filter_combination():
    filters = []
    for i in range(0, len(filter2field)):
        filters = filters + list(combinations(filter2field, i + 1))
    return filters


@pytest.mark.parametrize('combine', get_filter_combination())
def test_get_origin_merchant_list_with_combination_filters(admin_http_client, commission_db, set_up_merchant_message,
                                                           combine):
    params = {}
    filters = []
    for i in range(len(combine)):
        params.setdefault(combine[i][0], getattr(set_up_merchant_message[0], combine[i][1]))
        filters.append(getattr(MerchantMessage, combine[i][1]) == params[combine[i][0]])

    res = admin_http_client.get(url=API.GET_ORIGIN_MERCHANT_LIST, params=params)
    Verifier.verify_true(res['success'])

    merchant_message_list = commission_db.query(MerchantMessage).filter(*filters).all()
    Verifier.verify_equals(len(res['data']), len(merchant_message_list))

    for i in range(len(merchant_message_list)):
        validate_origin_merchant(res['data'][i], merchant_message_list[i])
