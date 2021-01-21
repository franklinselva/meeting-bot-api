### Using with a manage context

```python
with JWTZoomClient('API_KEY', 'API_SECRET') as client:
    user_list_response = client.users.list()
    ...
```

## Available methods

### Contacts

- client.contacts.list(...)
- client.contacts.list_external(...)

### Chat Channels

- client.chat_channels.list(...)
- client.chat_channels.create(...)
- client.chat_channels.update(...)
- client.chat_channels.delete(...)
- client.chat_channels.get(...)
- client.chat_channels.list_members(...)
- client.chat_channels.invite_members(...)
- client.chat_channels.join(...)
- client.chat_channels.leave(...)
- client.chat_channels.remove_member(...)

### Chat Messages

- client.chat_messages.list(...)
- client.chat_messages.post(...)
- client.chat_messages.update(...)
- client.chat_messages.delete(...)

### User

- client.user.create(...)
- client.user.cust_create(...)
- client.user.update(...)\*
- client.user.list(...)
- client.user.pending(...)
- client.user.get(...)
- client.user.get_by_email(...)

### Metting

- client.meeting.get(...)
- client.meeting.end(...)
- client.meeting.create(...)
- client.meeting.delete(...)
- client.meeting.list(...)
- client.meeting.update(...)

### Report

- client.report.get_account_report(...)
- client.report.get_user_report(...)

### Webinar

- client.webinar.create(...)
- client.webinar.update(...)
- client.webinar.delete(...)
- client.webinar.list(...)
- client.webinar.get(...)
- client.webinar.end(...)
- client.webinar.register(...)