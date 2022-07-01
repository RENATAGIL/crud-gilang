from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Task


# membuat class TaskForm untuk membuat task
class TaskForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Task
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('title', 'description', 'status')
        # mengatur teks label untuk setiap field
        labels = {
            'title': _('Judul'),
            'description': _('Deskripsi'),
            'status': _('Status')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'title': {
                'required': _("Judul harus diisi."),
            },
            'description': {
                'required': _("Deskripsi harus diisi."),
            },
        }

# def create_view(request):
#     # Mengecek method pada request
#     # Jika method-nya adalah POST, maka akan dijalankan
#     # proses validasi dan penyimpanan data
#     if request.method == 'POST':
#         # membuat objek dari class TaskForm
#         new_task = TaskForm(request.POST)
#         # Mengecek validasi form
#         if new_task.is_valid():
#             # Simpan data ke dalam table tasks
#             new_task.save()
#             # mengeset pesan sukses dan redirect ke halaman daftar task
#             messages.success(request, 'Sukses Menambah Task baru.')
#             return redirect('todo:index')
#     # Jika method-nya bukan POST
#     else:
#         # membuat objek dari class TaskForm
#         form = TaskForm()
#         # merender template form dengan memparsing data form
#         return render(request, 'todo/form.html', {'form': form})