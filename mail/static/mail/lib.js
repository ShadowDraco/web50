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
      responseField.innerHTML = result.message
    })
}

export const getSentEmails = async emails => {
  const response = await fetch('http://127.0.0.1:8000/emails/sent')
  const sentMail = await response.json()
  return sentMail
}

export const getInboxEmails = async () => {
  const response = await fetch('http://127.0.0.1:8000/emails/inbox')
  const inbox = await response.json()
  return inbox
}

export const getArchivedEmails = async () => {
  const response = await fetch('http://127.0.0.1:8000/emails/archive')
  const archive = await response.json()
  return archive
}

export const inspectEmail = async emailId => {
  // Show email view and hide other views
  document.querySelector('#emails-view').style.display = 'none'
  document.querySelector('#email-view').style.display = 'block'
  document.querySelector('#compose-view').style.display = 'none'

  const response = await fetch(`http://127.0.0.1:8000/emails/${emailId}`)
  const email = await response.json()

  const from = document.querySelector('#from')
  const to = document.querySelector('#to')
  const subject = document.querySelector('#subject')
  const timestamp = document.querySelector('#timestamp')
  const body = document.querySelector('#body')

  from.innerHTML = email.sender
  const recipients = ''
  email.recipients.map(recipient => {
    recipients = recipients + `, ${recipient}`
  })
  to.innerHTML = recipients
  subject.innerHTML = email.subject
  timestamp.innerHTML = email.timestamp
  body.innerHTML = email.body
}

export const populateEmailList = async getEmailFunction => {
  // Get Emails
  const emails = await getEmailFunction()
  const emailList = document.querySelector('#email-list')
  emailList.innerHTML = ''

  // Add Emails to page
  emails.forEach(email => {
    const liEl = document.createElement('li')
    liEl.addEventListener('click', () => {
      inspectEmail(email.id)
    })
    liEl.innerHTML = `
    <div class="title">
        <p class="sender">
            <strong>${email.sender}</strong>
        </p>
        <p class="subject">
            ${email.subject}
        </p>
    </div>
    <p class="timestamp">
        ${email.timestamp}
    </p>`
    emailList.appendChild(liEl)
  })
}
