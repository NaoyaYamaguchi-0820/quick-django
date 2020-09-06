from django import forms
from datetime import date
from .validates import compare_today
from .models import Book

class BookForm(forms.Form):

    isbn = forms.CharField(
        label='ISBNコード',
        required=True,
        max_length=20,
        error_messages={
            'required': 'ISBNコードは必須です',
            'max_length': 'ISBNコードは20文字以内で入力してください',
        }
    )

    title = forms.CharField(
        label='書名',
        required=True,
        max_length=100,
        error_messages={
            'required': '書名は必須です',
            'max_length': '書名は100文字以内で入力してください',
        }
    )

    price = forms.IntegerField(
        label='価格',
        required=True,
        min_value=0,
        error_messages={
            'required': '',
            'min_value': '価格は整数で入力してください',
        }
    )

    publisher = forms.ChoiceField(
        label='出版社',
        widget=forms.RadioSelect(),
        choices=[
            ('翔泳社', '翔泳社'),
            ('技術評論社', '技術評論社'),
            ('秀和システム', '秀和システム'),
            ('SBクリエイティブ', 'SBクリエイティブ'),
            ('日経BP', '日経BP'),
        ],
        error_messages={
            'required': '刊行日は必須です。',
            'invalid': '刊行日はYYYY-MM-DDの形式で入力してください',
        },
    )

    published = forms.DateField(
        label='刊行日',
        required=True,
        validators=[compare_today],
        error_messages={
            'required': '',

        }
    )

    def clean(self):
        cleaned_data = super().clean()
        isbn = cleaned_data.get('isbn')
        published = cleaned_data.get('published')

        if isbn and published:
            if published.year < 2007 and len(isbn) != 13:
                raise forms.ValidationError('刊行日が2007年より前の場合、ISBNコードは13桁です')
            elif published.year >= 2007 and len(isbn) != 17:
                raise forms.ValidationError('刊行日が2007年以降の場合、ISBNコードは17桁です')

class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'price', 'publisher', 'published')
