# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm


class Course(ndb.Model):
    name=ndb.StringProperty(required=True)


    @classmethod
    def query_order_by_name(cls):
        return cls.query().order(Course.name)

class CourseForm(ModelForm):
    _model_class = Course
    _include = [Course.name]



class Student(ndb.Model):
    name=ndb.StringProperty(required=True)
    birthday = ndb.StringProperty(required=True)
    phone_number = ndb.StringProperty(required=True)
    course = ndb.KeyProperty(required=True)

    @classmethod
    def query_order_by_name(cls):
        return cls.query().order(Student.name)

    @classmethod
    def query_by_course_order_by_name(cls, selected_course):
        if isinstance(selected_course, basestring):
            selected_course=ndb.Key(Course, int(selected_course))
        return cls.query(cls.course==selected_course).order(cls.name)


class StudentForm(ModelForm):
    _model_class = Student
    _include = [Student.name,
                Student.birthday,
                Student.phone_number,
                Student.course]
