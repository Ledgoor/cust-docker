$(document).ready(function(){
   var form = $('#search_form');
   console.log(form);

   form.on('submit', function(e){

      document.querySelector("#add").setAttribute("style", "display: none;");
      document.querySelector("#content").setAttribute("style", "display: none;");
      document.querySelector("#divresultSearch").setAttribute("style", "display: block;");


      var data = {
         'firstInputSearch': $('#firstInputSearch').val(),
      };

      var csrf_token = $('#search_form [name="csrfmiddlewaretoken"]').val();
      data["csrfmiddlewaretoken"] = csrf_token;

      var url = form.attr("action");

      $.ajax({
         url: url,
         type: 'POST',
         data: data,
         cache: true,
         success: function (data) {
            console.log("I get response")
            $("#resultSearch").html("").append(data.results)
         },
         error: function (data){
            console.log("Error response");
         }
      });
      e.preventDefault()
    })
 });