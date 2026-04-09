document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');
    var form = document.getElementById('meetingForm');
    var upcoming = document.getElementById('upcomingMeetings');
    var openButton = document.getElementById('openScheduleBtn');
    var noMeetingsText = document.getElementById('noMeetingsText');

    var titleInput = document.getElementById('meetingTitle');
    var dateInput = document.getElementById('meetingDate');
    var timeInput = document.getElementById('meetingTime');

    var modal = new bootstrap.Modal(document.getElementById('scheduleModal'));

    var savedMeetings = JSON.parse(localStorage.getItem('meetings')) || [];

    function openModal(selectedDate = '') {
        form.reset();
        dateInput.value = selectedDate;
        modal.show();
    }

    function updateNoMeetingsText() {
        if (upcoming.children.length > 0) {
            noMeetingsText.style.display = 'none';
        } else {
            noMeetingsText.style.display = 'block';
        }
    }

    function addMeetingToUI(meeting, index) {
        upcoming.insertAdjacentHTML('beforeend', `
            <div class="card mb-2 p-2 meeting-card" data-index="${index}">
                <strong>${meeting.title}</strong><br>
                Date: ${meeting.date}<br>
                Time: ${meeting.time}<br>
                <button class="btn btn-danger btn-sm mt-2 remove-btn">Remove</button>
            </div>
        `);

        updateNoMeetingsText();
    }

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',

        headerToolbar: {
            left: 'prev,today,next',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },

        events: meetingsFromDjango,

        dateClick: function (info) {
            openModal(info.dateStr);
        }
    });

    calendar.render();

    savedMeetings.forEach(function (meeting, index) {
        calendar.addEvent({
            id: String(index),
            title: meeting.title,
            start: meeting.dateTime
        });

        addMeetingToUI(meeting, index);
    });

    openButton.addEventListener('click', function () {
        openModal();
    });

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        var meeting = {
            title: titleInput.value,
            date: dateInput.value,
            time: timeInput.value,
            dateTime: dateInput.value + 'T' + timeInput.value
        };

        var index = savedMeetings.length;

        calendar.addEvent({
            id: String(index),
            title: meeting.title,
            start: meeting.dateTime
        });

        addMeetingToUI(meeting, index);

        savedMeetings.push(meeting);
        localStorage.setItem('meetings', JSON.stringify(savedMeetings));

        modal.hide();
        form.reset();
    });

    upcoming.addEventListener('click', function (e) {
        if (e.target.classList.contains('remove-btn')) {
            var card = e.target.closest('.meeting-card');
            var index = parseInt(card.getAttribute('data-index'));

            card.remove();

            var event = calendar.getEventById(String(index));
            if (event) {
                event.remove();
            }

            savedMeetings.splice(index, 1);
            localStorage.setItem('meetings', JSON.stringify(savedMeetings));

            updateNoMeetingsText();
            location.reload();
        }
    });

    updateNoMeetingsText();

});
// REMOVE BUTTON (works properly)
document.getElementById('upcomingMeetings').addEventListener('click', function (e) {

    if (e.target.classList.contains('remove-btn')) {

        // get the meeting card
        var card = e.target.closest('.meeting-card');

        // remove from UI
        card.remove();

    }

});