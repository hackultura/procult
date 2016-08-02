# -*- coding: utf-8 -*-

from django.test import TestCase
from django.db import models

from mptt.models import TreeForeignKey

from procult.notice.models import Category, Notice


class CategoryTest(TestCase):
    def test_should_have_uid_field(self):
        """Should have a field uid"""
        field = Category._meta.get_field('uid')
        self.assertIsInstance(field, models.UUIDField)

    def test_should_have_name_field(self):
        """Should have a field name"""
        field = Category._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)

    def test_should_have_parent_field(self):
        """Should have a field parent"""
        field = Category._meta.get_field('parent')
        self.assertIsInstance(field, TreeForeignKey)


class NoticeTest(TestCase):
    def test_should_have_uid_field(self):
        """Should have a field uid"""
        field = Notice._meta.get_field('uid')
        self.assertIsInstance(field, models.UUIDField)

    def test_should_have_name_field(self):
        """Should have a field name"""
        field = Notice._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)

    def test_should_have_categories_field(self):
        """Should have a field categories"""
        field = Notice._meta.get_field('categories')
        self.assertIsInstance(field, models.ManyToManyField)

    def test_should_have_resume_field(self):
        """Should have a field resume"""
        field = Notice._meta.get_field('resume')
        self.assertIsInstance(field, models.TextField)

    def test_should_have_notice_url_field(self):
        """Should have a field notice_url"""
        field = Notice._meta.get_field('notice_url')
        self.assertIsInstance(field, models.URLField)

    def test_should_have_start_publication_field(self):
        """Should have a field start_publication"""
        field = Notice._meta.get_field('start_publication')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_have_end_publication_field(self):
        """Should have a field end_publication"""
        field = Notice._meta.get_field('end_publication')
        self.assertIsInstance(field, models.DateTimeField)
