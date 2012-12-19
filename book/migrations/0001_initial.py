# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table('book_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ISBN13', self.gf('django.db.models.fields.CharField')(unique=True, max_length=14)),
        ))
        db.send_create_signal('book', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table('book_book')


    models = {
        'book.book': {
            'ISBN13': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '14'}),
            'Meta': {'object_name': 'Book'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['book']