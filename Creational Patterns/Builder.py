from dataclasses import dataclass, field


@dataclass()
class EmailMessage:
    to: str
    subject: str
    body: str
    cc: list[str] = field(default_factory=list)
    bcc: list[str] = field(default_factory=list)
    attachments: list[str] = field(default_factory=list)


class EmailBuilder:
    def __init__(self, to: str, subject: str, body: str):
        self._to = to
        self._subject = subject
        self._body = body
        self._cc: list[str] = []
        self._bcc: list[str] = []
        self._attachments: list[str] = []

    def add_cc(self, *recipients: str) -> "EmailBuilder":
        self._cc.extend(recipients)
        return self

    def add_bcc(self, *recipients: str) -> "EmailBuilder":
        self._bcc.extend(recipients)
        return self

    def add_attachment(self, *files: str) -> "EmailBuilder":
        self._attachments.extend(files)
        return self

    def build(self) -> EmailMessage:
        # Здесь можно добавить валидацию
        if not self._to or not self._subject or not self._body:
            raise ValueError("Обязательные поля не заполнены")
        return EmailMessage(
            to=self._to,
            subject=self._subject,
            body=self._body,
            cc=self._cc,
            bcc=self._bcc,
            attachments=self._attachments,
        )


if __name__ == '__main__':
    email = (
    EmailBuilder("user@example.com", "Тема", "Текст письма")
    .add_cc("manager@example.com")
    .add_bcc("secretary@example.com")
    .add_attachment("report.pdf", "chart.png")
    .build()
    )
    print(email)
