const btns = document.querySelectorAll('.btn');
const rbtns = document.querySelectorAll('#return-btn')
const csrftoken = getCookie('csrftoken')
// get all elements
let date_borrowed = new Date();
let return_date = new Date();
return_date.setDate(return_date.getDate() + 14)
console.log(user)

for (const btn of btns) {
  btn.addEventListener('click', function() {
    let id = btn.value
    fetch(`api/v1/borrow/${id}`, {
        method: 'PUT',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-type': "application/json; charset=UTF-8"
        },
        body: JSON.stringify({
            available: false,
            borrower: user,
            date_borrowed: formatDate(date_borrowed),
            return_date: formatDate(return_date)
        })
    })
    .then((res) => res.json())
    .then(json => console.log(json))
  });
}

for (const rbtn of rbtns) {
    rbtn.addEventListener('click', function() {
      let id = rbtn.value
      fetch(`api/v1/borrow/${id}`, {
          method: 'PUT',
          headers: {
              'X-CSRFToken': csrftoken,
              'Content-type': "application/json; charset=UTF-8"
          },
          body: JSON.stringify({
              available: true,
              borrower: null,
              date_borrowed: null,
              return_date: null
          })
      })
      .then((res) => res.json())
      .then(json => console.log(json))
    });
  }

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
}


