// static/js/task_tracker.js
document.getElementById('taskForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const taskId = document.getElementById('task_id').value;
    const method = taskId ? 'PUT' : 'POST';
    const url = taskId ? `/api/tasks/${taskId}/` : '/api/tasks/';

    const data = {
        name: document.getElementById('task_name').value,
        deadline: document.getElementById('task_deadline').value,
        event: document.getElementById('event_id').value,
        assigned_attendee: document.getElementById('attendee_id').value,
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
        alert('Error saving task');
    }
});

function editTask(id, name, deadline, status, assignedAttendeeId) {
    document.getElementById('task_id').value = id;
    document.getElementById('task_name').value = name;
    document.getElementById('task_deadline').value = deadline;
    document.getElementById('attendee_id').value = assignedAttendeeId;
}