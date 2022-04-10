from events.models import Event

e1 = Event(name='Tournoie de Billard')
e1.description = 'Tournoie de qualification'
e1.created_at = '2022-07-07 00:00:00'
e1.starts_at = '2022-07-10 14:00:00'
e1.ends_at = '2022-07-10 22:00:00'

e1.save()

e2 = Event(name='Qualification Européenne')
e2.description = 'Olympique de Marseille'
e2.created_at = '2022-08-07'
e2.starts_at = '2022-08-10 21:00:00'
e2.ends_at = '2022-08-15 22:30:00'

e2.save()