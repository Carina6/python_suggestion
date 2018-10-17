#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from datetime import date

TODAY = date.today()


class CommissionDate:
    @staticmethod
    def today():
        return TODAY.day

    @staticmethod
    def first_day_delta(months=0):
        month = (TODAY.month + months) % 12
        delta_years = (TODAY.month + months) // 12
        if month == 0:
            delta_years, month = delta_years - 1, 12

        return datetime.datetime(TODAY.year + delta_years, month, 1, 0, 0, 0)

    @staticmethod
    def first_day_delta_timestamp(months=0):
        first_day_delta = CommissionDate.first_day_delta(months=months)
        return int(first_day_delta.timestamp() * 1000)

    @staticmethod
    def date_delta(date_time=datetime.datetime.today(), years=0, months=0, days=0, hours=0, minutes=0, seconds=0,
                   microseconds=0):
        month = (date_time.month + months) % 12
        delta_years = (date_time.month + months) // 12
        if month == 0:
            delta_years, month = delta_years - 1, 12

        d_rep = date_time.replace(year=date_time.year + years + delta_years, month=month)

        return d_rep + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds,
                                          microseconds=microseconds)

    @staticmethod
    def date_delta_fmt(date_time=datetime.datetime.today(), years=0, months=0, days=0, hours=0, minutes=0, seconds=0,
                       microseconds=0, fmt="%Y-%m-%d %H:%M:%S"):
        date_delta = CommissionDate.date_delta(date_time=date_time, years=years, months=months, days=days, hours=hours,
                                               minutes=minutes, seconds=seconds, microseconds=microseconds)

        return date_delta.strftime(fmt)

    @staticmethod
    def date_delta_timestamp(years=0, months=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0):
        date_delta = CommissionDate.date_delta(years=years, months=months, days=days, hours=hours, minutes=minutes,
                                               seconds=seconds, microseconds=microseconds)
        return int(date_delta.timestamp() * 1000)

    @staticmethod
    def specify_date(year=TODAY.year, month=TODAY.month, day=TODAY.day):
        delta_years = month // 12
        month = month % 12
        if month == 0:
            delta_years, month = delta_years - 1, 12

        return datetime.datetime(year + delta_years, month, day, 0, 0, 0)

    @staticmethod
    def specify_date_timestamp(year=TODAY.year, month=TODAY.month, day=TODAY.day):
        specify_date = CommissionDate.specify_date(year=year, month=month, day=day)
        return int(specify_date.timestamp() * 1000)

    @staticmethod
    def tenth_day_for_next_month(timestamp):
        d = datetime.datetime.fromtimestamp(timestamp / 1000)

        return CommissionDate.specify_date_timestamp(year=d.year, month=d.month + 1, day=10)

    @staticmethod
    def tenth_day(timestamp):
        d = datetime.datetime.fromtimestamp(timestamp / 1000)

        return d.replace(day=10)


def test():
    print(CommissionDate.tenth_day(1535727600000))