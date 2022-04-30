searchSocket.onopen = function(e) {
    var status = document.getElementById('status');
    status.innerHTML = "🟢";
    console.log('Сокет открыт!');
};

searchSocket.onclose = function(e) {
    var status = document.getElementById('status');
    status.innerHTML = "🔴";
    document.querySelector('#button-disconnected').click();
    $("#results").html("").append('Соединение разорвано!' + '\n')
    console.error('Сокет разорван!');
};