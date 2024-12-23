
// const apiUrl = 'http://127.0.0.1:8000/api/'; // Update with your API base URL

// // Event Management Functions
// async function createEvent(event) {
//     const response = await fetch(apiUrl + 'events/', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(event),
//     });
//     if (!response.ok) {
//         console.error('Error creating event:', await response.json());
//     }
//     return response.json();
// }

// async function getEvents() {
//     const response = await fetch(apiUrl + 'events/');
//     if (!response.ok) {
//         console.error('Error fetching events:', await response.json());
//     }
//     return response.json();
// }

// async function updateEvent(eventId, event) {
//     const response = await fetch(apiUrl + 'events/' + eventId + '/', {
//         method: 'PUT',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(event),
//     });
//     if (!response.ok) {
//         console.error('Error updating event:', await response.json());
//     }
//     return response.json();
// }

// async function deleteEvent(eventId) {
//     const response = await fetch(apiUrl + 'events/' + eventId + '/', {
//         method: 'DELETE',
//     });
//     if (!response.ok) {
//         console.error('Error deleting event:', await response.json());
//     }
// }

// // Attendee Management Functions
// async function createAttendee(attendee) {
//     const response = await fetch(apiUrl + 'attendees/', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(attendee),
//     });
//     if (!response.ok) {
//         console.error('Error creating attendee:', await response.json());
//     }
//     return response.json();
// }

// async function getAttendees() {
//     const response = await fetch(apiUrl + 'attendees/');
//     if (!response.ok) {
//         console.error('Error fetching attendees:', await response.json());
//     }
//     return response.json();
// }

// async function updateAttendee(attendeeId, attendee) {
//     const response = await fetch(apiUrl + 'attendees/' + attendeeId + '/', {
//         method: 'PUT',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(attendee),
//     });
//     if (!response.ok) {
//         console.error('Error updating attendee:', await response.json());
//     }
//     return response.json();
// }

// async function deleteAttendee(attendeeId) {
//     const response = await fetch(apiUrl + 'attendees/' + attendeeId + '/', {
//         method: 'DELETE',
//     });
//     if (!response.ok) {
//         console.error('Error deleting attendee:', await response.json());
//     }
// }

// // Task Management Functions
// async function createTask(task) {
//     const response = await fetch(apiUrl + 'tasks/', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(task),
//     });
//     if (!response.ok) {
//         console.error('Error creating task:', await response.json());
//     }
//     return response.json();
// }

// async function getTasks(eventId) {
//     const response = await fetch(apiUrl + 'tasks/?event_id=' + eventId);
//     if (!response.ok) {
//         console.error('Error fetching tasks:', await response.json());
//     }
//     return response.json();
// }

// async function updateTaskStatus(taskId, status) {
//     const response = await fetch(apiUrl + 'tasks/' + taskId + '/', {
//         method: 'PATCH',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ status }),
//     });
//     if (!response.ok) {
//         console.error('Error updating task status:', await response.json());
//     }
//     return response.json();
// }

// // Show and Hide Forms
// function showEventForm(action) {
//     const form = document.getElementById('eventForm');
//     form.style.display = 'block';
//     if (action === 'update') {
//         const eventId = prompt("Enter Event ID to update:");
//         document.getElementById('event_id').value = eventId;
//         loadEventDetails(eventId);
//     } else {
//         form.reset();
//         document.getElementById('event_id').value = '';
//     }
// }

// function hideEventForm() {
//     document.getElementById('eventForm').style.display = 'none';
// }

// function showAttendeeForm(action) {
//     const form = document.getElementById('attendeeForm');
//     form.style.display = 'block';
//     if (action === 'update') {
//         const attendeeId = prompt("Enter Attendee ID to update:");
//         document.getElementById('attendee_id'). value = attendeeId;
//         loadAttendeeDetails(attendeeId);
//     } else {
//         form.reset();
//         document.getElementById('attendee_id').value = '';
//     }
// }

// function hideAttendeeForm() {
//     document.getElementById('attendeeForm').style.display = 'none';
// }

// function showTaskForm(action) {
//     const form = document.getElementById('taskForm');
//     form.style.display = 'block';
//     if (action === 'update') {
//         const taskId = prompt("Enter Task ID to update:");
//         document.getElementById('task_id').value = taskId;
//         loadTaskDetails(taskId);
//     } else {
//         form.reset();
//         document.getElementById('task_id').value = '';
//     }
// }

// function hideTaskForm() {
//     document.getElementById('taskForm').style.display = 'none';
// }

// // Load Functions
// async function loadEvents() {
//     const events = await getEvents();
//     const eventList = document.getElementById('eventList');
//     eventList.innerHTML = '';
//     events.forEach(event => {
//         const li = document.createElement('li');
//         li.innerHTML = `${event.name} <button onclick="deleteEvent(${event.id})">Delete</button>`;
//         eventList.appendChild(li);
//     });
// }

// async function loadAttendees() {
//     const attendees = await getAttendees();
//     const attendeeList = document.getElementById('attendeeList');
//     attendeeList.innerHTML = '';
//     attendees.forEach(attendee => {
//         const li = document.createElement('li');
//         li.innerHTML = `${attendee.name} (${attendee.email}) <button onclick="deleteAttendee(${attendee.id})">Delete</button>`;
//         attendeeList.appendChild(li);
//     });
// }

// async function loadTasks() {
//     const eventId = document.getElementById('task_event_id').value;
//     const tasks = await getTasks(eventId);
//     const taskList = document.getElementById('taskList');
//     taskList.innerHTML = '';
//     tasks.forEach(task => {
//         const li = document.createElement('li');
//         li.innerHTML = `${task.name} - Deadline: ${task.deadline} - Status: ${task.status} <button onclick="updateTaskStatus(${task.id}, '${task.status === 'Pending' ? 'Completed' : 'Pending'}')">Update Status</button>`;
//         taskList.appendChild(li);
//     });
// }

// // Handle Form Submissions
// async function handleEventSubmit(event) {
//     event.preventDefault();
//     const eventId = document.getElementById('event_id').value;
//     const newEvent = {
//         name: document.getElementById('event_name').value,
//         description: document.getElementById('event_description').value,
//         location: document.getElementById('event_location').value,
//         date: document.getElementById('event_date').value,
//     };
//     if (eventId) {
//         await updateEvent(eventId, newEvent);
//     } else {
//         await createEvent(newEvent);
//     }
//     hideEventForm();
//     loadEvents();
// }

// async function handleAttendeeSubmit(event) {
//     event.preventDefault();
//     const attendeeId = document.getElementById('attendee_id').value;
//     const newAttendee = {
//         name: document.getElementById('attendee_name').value,
//         email: document.getElementById('attendee_email').value,
//     };
//     if (attendeeId) {
//         await updateAttendee(attendeeId, newAttendee);
//     } else {
//         await createAttendee(newAttendee);
//     }
//     hideAttendeeForm();
//     loadAttendees();
// }

// async function handleTaskSubmit(event) {
//     event.preventDefault();
//     const taskId = document.getElementById('task_id').value;
//     const newTask = {
//         name: document.getElementById('task_name').value,
//         deadline: document.getElementById('task_deadline').value,
//         event_id: document.getElementById('task_event_id').value,
//     };
//     if (taskId) {
//         await updateTask(taskId, newTask);
//     } else {
//         await createTask(newTask);
//     }
//     hideTaskForm();
//     loadTasks();
// }

// // Load initial data
// document.addEventListener('DOMContentLoaded', () => {
//     loadEvents();
//     loadAttendees();
//     loadTasks(); // You may want to pass a specific event ID here to load tasks for that event
// });
const apiUrl = 'http://127.0.0.1:8000/api/'; // Update with your API base URL

// Event Management Functions
async function createEvent(event) {
    const response = await fetch (apiUrl + 'events/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(event),
    });
    if (!response.ok) {
        console.error('Error creating event:', await response.json());
    }
    return response.json();
}

async function getEvents() {
    const response = await fetch(apiUrl + 'events/');
    if (!response.ok) {
        console.error('Error fetching events:', await response.json());
    }
    return response.json();
}

async function updateEvent(eventId, event) {
    const response = await fetch(apiUrl + 'events/' + eventId + '/', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(event),
    });
    if (!response.ok) {
        console.error('Error updating event:', await response.json());
    }
    return response.json();
}

async function deleteEvent(eventId) {
    const response = await fetch(apiUrl + 'events/' + eventId + '/', {
        method: 'DELETE',
    });
    if (!response.ok) {
        console.error('Error deleting event:', await response.json());
    }
}

// Attendee Management Functions
async function createAttendee(attendee) {
    const response = await fetch(apiUrl + 'attendees/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(attendee),
    });
    if (!response.ok) {
        console.error('Error creating attendee:', await response.json());
    }
    return response.json();
}

async function getAttendees() {
    const response = await fetch(apiUrl + 'attendees/');
    if (!response.ok) {
        console.error('Error fetching attendees:', await response.json());
    }
    return response.json();
}

async function updateAttendee(attendeeId, attendee) {
    const response = await fetch(apiUrl + 'attendees/' + attendeeId + '/', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(attendee),
    });
    if (!response.ok) {
        console.error('Error updating attendee:', await response.json());
    }
    return response.json();
}

async function deleteAttendee(attendeeId) {
    const response = await fetch(apiUrl + 'attendees/' + attendeeId + '/', {
        method: 'DELETE',
    });
    if (!response.ok) {
        console.error('Error deleting attendee:', await response.json());
    }
}

// Task Management Functions
async function createTask(task) {
    const response = await fetch(apiUrl + 'tasks/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(task),
    });
    if (!response.ok) {
        console.error('Error creating task:', await response.json());
    }
    return response.json();
}

async function getTasks(eventId) {
    const response = await fetch(apiUrl + 'tasks/?event_id=' + eventId);
    if (!response.ok) {
        console.error('Error fetching tasks:', await response.json());
    }
    return response.json();
}

async function updateTaskStatus(taskId, status) {
    const response = await fetch(apiUrl + 'tasks/' + taskId + '/', {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status }),
    });
    if (!response.ok) {
        console.error('Error updating task status:', await response.json());
    }
    return response.json();
}

// Show and Hide Forms
function showEventForm(action) {
    const form = document.getElementById('eventForm');
    form.style.display = 'block';
    if (action === 'update') {
        const eventId = prompt("Enter Event ID to update:");
        document.getElementById('event_id').value = eventId;
        loadEventDetails(eventId);
    } else {
        form.reset();
        document.getElementById('event_id').value = '';
    }
}

function hideEventForm() {
    document.getElementById('eventForm').style.display = 'none';
}

function showAttendeeForm(action) {
    const form = document.getElementById('attendeeForm');
    form.style.display = 'block';
    if (action === 'update') {
        const attendeeId = prompt("Enter Attendee ID to update:");
        document.getElementById('attendee_id').value = attendeeId;
        loadAttendeeDetails(attendeeId);
    } else {
        form.reset();
        document.getElementById('attendee_id').value = '';
    }
}

function hideAttendeeForm() {
    document.getElementById('attendeeForm').style.display = 'none';
}

function showTaskForm(action) 
{
    const form = document.getElementById('taskForm');
    form.style.display = 'block';
    if (action === 'update') {
        const taskId = prompt("Enter Task ID to update:");
        document.getElementById('task_id').value = taskId;
        loadTaskDetails(taskId);
    } else {
        form.reset();
        document.getElementById('task_id').value = '';
    }
}

function hideTaskForm() {
    document.getElementById('taskForm').style.display = 'none';
}

// Load Functions
async function loadEvents() {
    const events = await getEvents();
    const eventList = document.getElementById('eventList');
    eventList.innerHTML = '';
    events.forEach(event => {
        const li = document.createElement('li');
        li.innerHTML = `${event.name} <button onclick="editEvent('${event.id}', '${event.name}', '${event.description}', '${event.location}', '${event.date}')">Edit</button> <button onclick="deleteEvent('${event.id}')">Delete</button>`;
        eventList.appendChild(li);
    });
}

async function loadAttendees() {
    const attendees = await getAttendees();
    const attendeeList = document.getElementById('attendeeList');
    attendeeList.innerHTML = '';
    attendees.forEach(attendee => {
        const li = document.createElement('li');
        li.innerHTML = `${attendee.name} (${attendee.email}) <button onclick="editAttendee(${attendee.id}, '${attendee.name}', '${attendee.email}')">Edit</button> <button onclick="deleteAttendee(${attendee.id})">Delete</button>`;
        attendeeList.appendChild(li);
    });
}

async function loadTasks() {
    const eventId = document.getElementById('task_event_id').value;
    const tasks = await getTasks(eventId);
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.innerHTML = `${task.name} - Deadline: ${task.deadline} - Status: ${task.status} <button onclick="updateTaskStatus(${task.id}, '${task.status === 'Pending' ? 'Completed' : 'Pending'}')">Update Status</button>`;
        taskList.appendChild(li);
    });
}

// Handle Form Submissions
async function handleEventSubmit(event) {
    event.preventDefault();
    const eventId = document.getElementById('event_id').value;
    const newEvent = {
        name: document.getElementById('event_name').value,
        description: document.getElementById('event_description').value,
        location: document.getElementById('event_location').value,
        date: document.getElementById('event_date').value,
    };
    if (eventId) {
        await updateEvent(eventId, newEvent);
    } else {
        await createEvent(newEvent);
    }
    hideEventForm();
    loadEvents();
}

async function handleAttendeeSubmit(event) {
    event.preventDefault();
    const attendeeId = document.getElementById('attendee_id').value;
    const newAttendee = {
        name: document.getElementById('attendee_name').value,
        email: document.getElementById('attendee_email').value,
    };
    if (attendeeId) {
        await updateAttendee(attendeeId, newAttendee);
    } else {
        await createAttendee(newAttendee);
    }
    hideAttendeeForm();
    loadAttendees();
}

async function handleTaskSubmit(event) {
    event.preventDefault();
    const taskId = document.getElementById('task_id').value;
    const newTask = {
        name: document.getElementById('task_name').value,
        deadline: document.getElementById('task_deadline').value,
        event_id: document.getElementById('task_event_id').value,
        attendee_id: document.getElementById('attendee_id').value,
        status: document.getElementById('task_status').value,
    };
    if (taskId) {
        await updateTask(taskId, newTask);
    } else {
        await createTask(newTask);
    }
    hideTaskForm();
    loadTasks();
}

// Load initial data
document.addEventListener('DOMContentLoaded', () => {
    loadEvents();
    loadAttendees();
    loadTasks(); // You may want to pass a specific event ID here to load tasks for that event
});