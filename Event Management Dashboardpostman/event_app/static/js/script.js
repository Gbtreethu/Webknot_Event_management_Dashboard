async function fetchEvents() {
    const response = await fetch('/api/events/');
    const events = await response.json();
    const eventList = document.getElementById('eventList');
    eventList.innerHTML = '';
    events.forEach(event => {
        const li = document.createElement('li');
        li.innerHTML = `<strong>${event.name}</strong> - ${event.description} - ${event.location} - ${event.date}`;
        eventList.appendChild(li);
    });
}

// Call fetchEvents on page load
document.addEventListener('DOMContentLoaded', fetchEvents);
function editEvent(id, name, description, location, date) {
    document.getElementById('event_id').value = id;
    document.querySelector('input[name="name"]').value = name;
    document.querySelector('textarea[name="description"]').value = description;
    document.querySelector('input[name="location"]').value = location;
    document.querySelector('input[name="date"]').value = date;
}

function editAttendee(id, name, email) {
    document.getElementById('attendee_id').value = id;
    document.querySelector('input[name="name"]').value = name;
    document.querySelector('input[name="email"]').value = email;
}

function editTask(id, name, deadline, status) {
    document.getElementById('task_id').value = id;
    document.querySelector('input[name="name"]').value = name;
    document.querySelector('input[name="deadline"]').value = deadline;
    document.querySelector('select[name="status"]').value = status;
}