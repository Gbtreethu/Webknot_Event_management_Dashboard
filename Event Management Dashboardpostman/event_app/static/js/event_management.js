
const apiUrl = 'http://127.0.0.1:8000/api/'; // Update with your API base URL

// Show the form for adding a new event
function showAddForm() {
    document.getElementById('addEventForm').classList.remove('hidden');
    document.getElementById('eventTable').classList.add('hidden');
    document.getElementById('eventForm').reset(); // Reset the form
}

// Show the event table
function showEventTable() {
    document.getElementById('eventTable').classList.remove('hidden');
    document.getElementById('addEventForm').classList.add('hidden');
}

// Create a new event
async function createEvent(event) {
    const response = await fetch(apiUrl + 'events/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(event),
    });
    if (!response.ok) {
        console.error('Error creating event:', await response.json());
        throw new Error('Failed to create event');
    }
    return response.json();
}

// Get all events
async function getEvents() {
    const response = await fetch(apiUrl + 'events/');
    if (!response.ok) {
        console.error('Error fetching events:', await response.json());
        throw new Error('Failed to fetch events');
    }
    return response.json();
}

// Update an existing event
async function updateEvent(eventId, event) {
    const response = await fetch(apiUrl + 'events/' + eventId + '/', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(event),
    });
    if (!response.ok) {
        console.error('Error updating event:', await response.json());
        throw new Error('Failed to update event');
    }
    return response.json();
}

// Delete an event
async function deleteEvent(eventId) {
    const response = await fetch(apiUrl + 'events/' + eventId + '/', {
        method: 'DELETE',
    });
    if (!response.ok) {
        console.error('Error deleting event:', await response.json());
        throw new Error('Failed to delete event');
    }
}

// Handle form submission
// async function handleEventSubmit(event) {
//     event.preventDefault(); // Prevent the form from submitting the traditional way
//     const formData = new FormData(event.target);
//     const eventId = formData.get('event_id');

//     const newEvent = {
//         name: formData.get('name'),
//         description: formData.get('description'),
//         location: formData.get('location'),
//         date: formData.get('date'),
//     };

//     try {
//         if (eventId) {
//             // Update existing event
//             await updateEvent(eventId, newEvent);
//             updateEventInTable(eventId, newEvent);
//         } else {
//             // Create new event
//             const eventData = await createEvent(newEvent);
//             addEventToTable(eventData);
//         }
//         document.getElementById('eventForm').reset(); // Reset the form
//         showEventTable(); // Show the event table after submission
//     } catch (error) {
//         alert(error.message); // Display error message to the user
//     }
// }
// Handle form submission
async function handleEventSubmit(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way
    const formData = new FormData(event.target);
    const eventId = formData.get('event_id');

    const newEvent = {
        name: formData.get('name'),
        description: formData.get('description'),
        location: formData.get('location'),
        date: formData.get('date'),
    };

    try {
        if (eventId) {
            // Update existing event
            await updateEvent(eventId, newEvent);
            updateEventInTable(eventId, newEvent);
        } else {
            // Create new event
            const eventData = await createEvent(newEvent);
            addEventToTable(eventData);
        }
        document.getElementById('eventForm').reset(); // Reset the form
        showEventTable(); // Show the event table after submission
    } catch (error) {
        alert(error.message); // Display error message to the user
    }
}
// Load initial data
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const events = await getEvents();
        events.forEach(addEventToTable);
    } catch (error) {
        alert(error.message); // Display error message to the user
    }
});

// Add event to the table
function addEventToTable(eventData) {
    const eventList = document.getElementById('eventList');
    
    // Check if the event already exists in the table
    if (document.getElementById(`event-${eventData.id}`)) {
        return; // If it exists, do not add it again
    }

    const newRow = document.createElement('tr');
    newRow.id = `event-${eventData.id}`;
    newRow.innerHTML = `
        <td>${eventData.name}</td>
        <td>${eventData.description}</td>
        <td>${eventData.location}</td>
        <td>${eventData.date}</td>
        <td>
            <button onclick="editEvent('${eventData.id}', '${eventData.name}', '${eventData.description}', '${eventData.location}', '${eventData.date}')">Edit</button>
            <button onclick="confirmDeleteEvent('${eventData.id}')">Delete</button>
        </td>
    `;
    eventList.appendChild(newRow);
}

// Update existing event in the table
function updateEventInTable(eventId, eventData) {
    const eventRow = document.getElementById(`event-${eventId}`);
    eventRow.innerHTML = `
        <td>${eventData.name}</td>
        <td>${eventData.description}</td>
        <td>${eventData.location}</td>
        <td>${eventData.date}</td>
        <td>
            <button onclick="editEvent('${eventId}', '${eventData.name}', '${eventData.description}', '${eventData.location}', '${eventData.date}')">Edit</button>
            <button onclick="confirmDeleteEvent('${eventId}')">Delete</button>
        </td>
    `;
}
document.getElementById('eventForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const eventId = document.getElementById('event_id').value;
    const method = eventId ? 'PUT' : 'POST';
    const url = eventId ? `/api/events/${eventId}/` : '/api/events/';

    const data = {
        name: document.getElementById('event_name').value,
        description: document.getElementById('event_description').value,
        location: document.getElementById('event_location').value,
        date : document.getElementById('event_date').value,
    };

    const response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        window.location.reload();
    } else {
        alert('Error saving event');
    }
});

// Edit event
function editEvent(id, name, description, location, date) {
    // document.getElementById('event_id').value = id;
    // document.getElementById('event_name').value = name;
    // document.getElementById('event_description').value = description;
    // document.getElementById('event_location').value = location;
    // document.getElementById('event_date').value = date.split('T')[0]; // Format date for input
    // showAddForm(); // Show the form for editing
// Set the values of the form fields to the existing event data
document.getElementById('event_id').value = id;
document.getElementById('event_name').value = name;
document.getElementById('event_description').value = description;
document.getElementById('event_location').value = location;

// Ensure the date is in the correct format for the input field
document.getElementById('event_date').value = date; // Assuming date is in 'YYYY-MM-DD' format
document.getElementById('formTitle').innerText = 'Update Event';
    document.getElementById('submitButton').innerText = 'Update';

// Show the form for editing
showAddForm();


}

// Confirm delete event
function confirmDeleteEvent(id) {
    if (confirm('Are you sure you want to delete this event?')) {
        deleteEventById(id);
    }
}

// Delete event by ID
async function deleteEventById(id) {
    try {
        await deleteEvent(id);
        const eventRow = document.getElementById(`event-${id}`);
        eventRow.remove(); // Remove the event from the table
    } catch (error) {
        alert(error.message); // Display error message to the user
    }
}