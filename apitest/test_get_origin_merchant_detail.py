#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from model.stone_commission.models import MerchantMessage
from tests.retail_loan.commission.merchant.validator import validate_origin_merchant_detail, validate_origin_shop_detail
from xutils.verifier import Verifier
from .api import API


def test_get_origin_merchant_detail(admin_http_client, commission_db, set_up_merchant_message):
    merchant_id = set_up_merchant_message[0].shop_no
    res = admin_http_client.get(url=API.GET_ORIGIN_MERCHANT_DETAIL, params=dict(merchantId=merchant_id))
    Verifier.verify_true(res['success'])

    merchant_message_list = commission_db.query(MerchantMessage).filter(MerchantMessage.shop_no == merchant_id).all()
    Verifier.verify_equals(len(res['singleData']['shops']), len(merchant_message_list))
    validate_origin_merchant_detail(res['singleData']['merchant'], merchant_message_list[0])
    for i in range(len(merchant_message_list)):
        validate_origin_shop_detail(res['singleData']['shops'][i], merchant_message_list[i])


@pytest.mark.parametrize('merchant_id', [None, ''])
def test_get_merchant_detail_without_contract_id(admin_http_client, merchant_id):
    res = admin_http_client.get(url=API.GET_ORIGIN_MERCHANT_DETAIL, params=dict(merchantId=merchant_id))
    Verifier.verify_false(res['success'])
    Verifier.verify_equals(res['error'], '缺少参数')

