var formattedFormData2={};
var occasionValLS;
var cityValLS;
$(document).ready(function(){
	$('#Myimg').click(function(){
  		$('#Mymodal').modal('show')
	});
	//const favourites = new Set()
	$('button').click(function(e){
		function msgout(){
			sid=document.getElementById("fav_msg").innerHTML="";

		}
		

		

		let buttonId=this.id;

		if(buttonId.slice(0,9)=="favourite"){

		sid=document.getElementById("fav_msg").innerHTML="Favourite Added Successfully!"
		setTimeout(msgout, 1000);

		let idx=buttonId.slice(9);
		let imgsrc=document.getElementById("Myimg"+idx).src;
		//favourites.add(imgsrc);

		formattedFormData2["favouriteUrl"]=imgsrc
		occasionValLS=localStorage.getItem("occasionVal");
		cityValLS=localStorage.getItem("cityVal");
		formattedFormData2["occasion"]=occasionValLS
		formattedFormData2["city"]=cityValLS
		formattedFormData2["actionToBePerformed"] = "ADD_NEW_FAVOURITES"
		formData = JSON.stringify(formattedFormData2)
		console.log(formData)
		e.preventDefault();
		$.ajax({
			type:"POST",
            url:"/favourites",
            data:formData,
            success:function(){
				return "success"
                
            },
			dataType: "json",
            contentType : "application/json"
		})
	}else{

		alert("shop")


	}

	});
	
	
});