// // static/js/attendee_management.js
// document.getElementById('attendeeForm').addEventListener('submit', async function(event) {
//     event.preventDefault();
//     const attendeeId = document.getElementById('attendee_id').value;
//     const method = attendeeId ? 'PUT' : 'POST';
//     const url = attendeeId ? `/api/attendees/${attendeeId}/` : '/api/attendees/';

//     const data = {
//         name: document.getElementById('attendee_name').value,
//         email: document.getElementById('attendee_email').value,
//     };

//     const response = await fetch(url, {
//         method: method,
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//     });

//     if (response.ok) {
//         window.location.reload();
//     } else {
//         alert('Error saving attendee');
//     }
// });

// function editAttendee(id, name, email) {
//     document.getElementById('attendee_id').value = id;
//     document.getElementById('attendee_name').value = name;
//     document.getElementById('attendee_email').value = email;
// }







const apiUrl = 'http://127.0.0.1:8000/api/'; // Update with your API base URL

// Show the form for adding a new attendee
function showAddAttendeeForm() {
    document.getElementById('addAttendeeForm').classList.remove('hidden');
    document.getElementById('attendeeTable').classList.add('hidden');
    document.getElementById('addAttendeeForm').reset(); // Reset the form
}

// Show the attendee table
function showAttendeeTable() {
    document.getElementById('attendeeTable').classList.remove('hidden');
    document.getElementById('addAttendeeForm').classList.add('hidden');
}

// Create a new attendee
async function createAttendee(attendee) {
    const response = await fetch(apiUrl + 'attendees/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(attendee),
    });
    if (!response.ok) {
        console.error('Error creating attendee:', await response.json());
        throw new Error('Failed to create attendee');
    }
    return response.json();
}

// Get all attendees
async function getAttendees() {
    const response = await fetch(apiUrl + 'attendees/');
    if (!response.ok) {
        console.error('Error fetching attendees:', await response.json());
        throw new Error('Failed to fetch attendees');
    }
    return response.json();
}

// Update an existing attendee
async function updateAttendee(attendeeId, attendee) {
    const response = await fetch(apiUrl + 'attendees/' + attendeeId + '/', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(attendee),
    });
    if (!response.ok) {
        console.error('Error updating attendee:', await response.json());
        throw new Error('Failed to update attendee');
    }
    return response.json();
}

// Delete an attendee
async function deleteAttendee(attendeeId) {
    const response = await fetch(apiUrl + 'attendees/' + attendeeId + '/', {
        method: 'DELETE',
    });
    if (!response.ok) {
        console.error('Error deleting attendee:', await response.json());
        throw new Error('Failed to delete attendee');
    }
}

// Load attendees and display them in a table
async function loadAttendees() {
    try {
        const attendees = await getAttendees();
        const attendeeTableBody = document.getElementById('attendeeTableBody');
        attendeeTableBody.innerHTML = ''; // Clear existing rows

        attendees.forEach(attendee => {
            const row = document.createElement('tr');
            row.innerHTML = `
                < td>${attendee.name}</td>
                <td>${attendee.email}</td>
                <td>
                    <button onclick="editAttendee(${attendee.id}, '${attendee.name}', '${attendee.email}')">Edit</button>
                    <button onclick="confirmDeleteAttendee(${attendee.id})">Delete</button>
                </td>
            `;
            attendeeTableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error loading attendees:', error);
    }
}

// Confirm deletion of an attendee
function confirmDeleteAttendee(attendeeId) {
    if (confirm('Are you sure you want to delete this attendee?')) {
        deleteAttendee(attendeeId)
            .then(() => {
                loadAttendees(); // Reload attendees after deletion
                displayMessage('Attendee deleted successfully', 'success');
            })
            .catch(error => {
                console.error('Error deleting attendee:', error);
                displayMessage('Failed to delete attendee', 'error');
            });
    }
}

// Edit an attendee
function editAttendee(id, name, email) {
    document.getElementById('attendee_id').value = id;
    document.getElementById('attendee_name').value = name;
    document.getElementById('attendee_email').value = email;
    showAddAttendeeForm(); // Show the form to edit
}

// Display success or error messages
function displayMessage(message, type) {
    const messageContainer = document.getElementById('messageContainer');
    messageContainer.innerHTML = `<div class="${type}">${message}</div>`;
    setTimeout(() => {
        messageContainer.innerHTML = '';
    }, 3000);
}

// Handle form submission
document.getElementById('addAttendeeForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const attendeeId = document.getElementById('attendee_id').value;
    const attendee = {
        name: document.getElementById('attendee_name').value,
        email: document.getElementById('attendee_email').value,
    };

    try {
        if (attendeeId) {
            await updateAttendee(attendeeId, attendee);
            displayMessage('Attendee updated successfully', 'success');
        } else {
            await createAttendee(attendee);
            displayMessage('Attendee added successfully', 'success');
        }
        loadAttendees(); // Reload attendees after adding/updating
        showAttendeeTable(); // Show the attendee table
    } catch (error) {
        console.error('Error saving attendee:', error);
        displayMessage('Failed to save attendee', 'error');
    }
});

// Call loadAttendees on page load to populate the table
document.addEventListener('DOMContentLoaded', loadAttendees);
