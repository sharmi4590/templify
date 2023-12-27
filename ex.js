document.getElementById('invitation-form').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var eventTitle = document.getElementById('event-title').value;
    var eventDate = document.getElementById('event-date').value;
  
    var invitation = document.createElement('div');
    invitation.classList.add('invitation');
    invitation.innerHTML = `
      <h2>${eventTitle}</h2>
      <p>Date: ${eventDate}</p>
      <!-- Additional invitation details -->
  
      <button>Send Invitation</button>
    `;
  
    document.getElementById('invitation-preview').innerHTML = '';
    document.getElementById('invitation-preview').appendChild(invitation);
  });
  