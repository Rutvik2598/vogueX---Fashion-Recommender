$(document).ready(function(){
    $(".recoButton1").click(function(e){
        var formData = $('#recoForm').serializeArray();
        var formattedFormData = {};
        for(var i = 0; i < formData.length; i++){
            formattedFormData[formData[i]["name"]] = formData[i]["value"];
        }
        console.log(formattedFormData);
        formData = JSON.stringify(formattedFormData)
        console.log(formData);
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/recommendations",
            data: formData,
            success: function(data){
                
                var str = "";
                for(var i = 0; i < data["links"].length; i++){
                    str += data["links"][i] + " || ";
                }
                console.log(data["links"]);
                var redirectUrl = window.location.protocol + "//" + window.location.host + "/results?" + str;
                location.href = redirectUrl;
            },
            dataType: "json",
            contentType : "application/json"
        });
    });
    $(".recoButton1").click(function(e){
        var loader= document.getElementById( 'center' )
        loader.style.display = '';
    });
});
