from django.contrib import admin
from catalog.models import Author, Book, BookInstance, Genre, Language

admin.site.register(Genre)
admin.site.register(Language)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    exclude = ['genre', 'summary']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline, ]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline, ]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'imprint', 'book')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
