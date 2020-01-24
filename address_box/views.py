from django.shortcuts import render, redirect
from .models import Person, Email, Group
from django.views import View
from .forms import PersonForm, EmailForm

# Create your views here.


class NewPerson(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'add_person.html', {'form': form})

    def post(self, request):
        f = PersonForm(request.POST)
        if f.is_valid():
            first = f.cleaned_data['first_name']
            last = f.cleaned_data['last_name']
            description = f.cleaned_data['description']
            person = Person.objects.create(first_name=first, last_name=last, description=description)
            person.save()
            return redirect('show-all')


class DelPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        person.delete()
        return redirect('show-all')


class ShowPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        emails = Email.objects.filter(owner=person)
        groups = person.group_set.all()
        return render(request, 'show_person.html', {'person': person, 'emails': emails, 'groups': groups})


class AllPerson(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'all_persons.html', {'persons': persons})


class Groups(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'all_groups.html', {'groups': groups})


class AddGroup(View):

    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'add_group.html', {'members': persons})

    def post(self, request):
        name = request.POST['name']
        group, created = Group.objects.get_or_create(name=name)
        group.save()
        members = [Person.objects.get(id=int(i)) for i in request.POST.getlist('members')]
        group.members.set(members)
        group.save()
        return redirect('groups')


class ShowGroup(View):

    def get(self, request, id):
        group = Group.objects.get(id=id)
        members = list(group.members.all())
        return render(request, 'show_group.html', {'group': group, 'members': members})


class DelGroup(View):

    def get(self, request, id):
        group = Group.objects.get(id=id)
        group.delete()
        return redirect('groups')


class DelMemberFromGroup(View):

    def get(self, request, g_id, m_id):
        group = Group.objects.get(id=g_id)
        member = Person.objects.get(id=m_id)
        group.members.remove(member)
        group.save()
        return redirect('show-group', id=group.id)


class AddEmail(View):

    def get(self, request, id):
        f = EmailForm()
        return render(request, 'add_email.html', {'form': f})

    def post(self, request, id):
        f = EmailForm(request.POST)
        person = Person.objects.get(id=id)
        if f.is_valid():
            email = f.cleaned_data['email']
            email_type = f.cleaned_data['type']
            email_obj, created = Email.objects.get_or_create(email=email, type=email_type, owner=person)
            if not created:
                email_obj.save()
        return redirect('show-person', id=person.id)


class AddGroupToPerson(View):

    def get(self, request, id):
        groups = Group.objects.all()
        return render(request, 'add_groups.html', {'groups': groups})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        groups = [Group.objects.get(id=int(i)) for i in request.POST.getlist('groups')]
        person.group_set.set(groups)
        person.save()
        return redirect('show-person', id=person.id)