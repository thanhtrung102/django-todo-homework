from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo
from django.utils import timezone

class TodoTests(TestCase):
    def setUp(self):
        # Create a sample task to use in our tests
        self.todo = Todo.objects.create(
            title="Test Task", 
            due_date=timezone.now()
        )
        self.client = Client()

    def test_model_content(self):
        # Check if the model is created correctly
        self.assertEqual(self.todo.title, "Test Task")
        self.assertFalse(self.todo.is_resolved)

    def test_homepage_list(self):
        # Check if the homepage loads and contains our task
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_create_todo(self):
        # Test creating a new task via the form
        response = self.client.post(reverse('todo_create'), {
            'title': 'New Task',
            'due_date': '2025-12-31 12:00:00'
        })
        # It should redirect to the list page after success (Status 302)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Todo.objects.count(), 2) # We had 1, now we have 2

    def test_delete_todo(self):
        # Test deleting a task
        response = self.client.post(reverse('todo_delete', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302) # Redirects after delete
        self.assertEqual(Todo.objects.count(), 0)

    def test_mark_resolved(self):
        # Test toggling the resolution status
        response = self.client.post(reverse('todo_toggle_status', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        
        # Reload the task from the database to check the new value
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_resolved)