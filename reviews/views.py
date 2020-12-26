from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from .models import Review


# def reviews(request):
#     return render(request, 'reviews/reviews.html')


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']


class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'review', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

