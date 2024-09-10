export const sendEmail = async event => {
  const responseField = document.querySelector('#response-field')

  const recipients = event.target[1].value
  const subject = event.target[2].value
  const body = event.target[3].value

  fetch('http://127.0.0.1:8000/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body,
    }),
  })
    .then(response => response.json())
    .then(result => {
      // Print result
      console.log(result)
      responseField.innerHTML = result.message
    })
}

export const getSentEmails = async () => {
  const response = await fetch('http://127.0.0.1:8000/emails/sent')
  const sentMail = await response.json()
}

export const getInboxEmails = async () => {
  const response = await fetch('http://127.0.0.1:8000/emails/inbox')
  const inbox = await response.json()
}

export const getArchivedEmails = async () => {
  const response = await fetch('http://127.0.0.1:8000/emails/archive')
  const archive = await response.json()
}
