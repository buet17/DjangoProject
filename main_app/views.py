from django.shortcuts import render, HttpResponse

from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Book
from django.shortcuts import redirect, render
from .forms import BookForm
from io import BytesIO


# Create your views here.

# def home(request):
#     return render(request,'home.html')
    
def service(request):
    return render(request,'service.html')

def welcome(request):
    return HttpResponse('Hello World!')
    
# Creating PDF views


 
def home(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    # Redirect to PDF generation after adding a book
            return redirect('home_page')  
    else:
        form = BookForm()
    return render(request, 'home.html', 
    # return render(request, 'myapp/create_user_profile.html', 
                  {'form': form})
 
def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), 
                            as_attachment=True, 
                            filename='book_catalog.pdf')
    return response
 
 
def generate_pdf_file():
    # from io import BytesIO
 
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
 
    # Create a PDF document
    books = Book.objects.all()
    p.drawString(100, 750, "Book Catalog")
 
    y = 700
    for book in books:
        p.drawString(100, y, f"Title: {book.title}")
        p.drawString(100, y - 20, f"Author: {book.author}")
        p.drawString(100, y - 40, f"Year: {book.publication_year}")
        y -= 60
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer

# csvapp/views.py 
import csv 
from django.http import HttpResponse 
from .models import Book 
  
def generate_csv(request): 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment; filename="book_catalog.csv"'
  
    writer = csv.writer(response) 
    writer.writerow(['Title', 'Author', 'Publication Year']) 
  
    books = Book.objects.all() 
    for book in books: 
        writer.writerow([book.title, book.author, book.publication_year]) 
  
    return response 