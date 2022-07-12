function hide_section_A(){
    // show div based on incoterms
    var sectionA = document.getElementsByClassName("sectionA");
    for(let i = 0 ; i<sectionA.length;i++){
    sectionA[i].style.display = "none";
    
   }
}

function hide_section_B(){
    // show div based on incoterms
    var sectionB = document.getElementsByClassName("sectionB");
    for(let i = 0 ; i<sectionB.length;i++){
    sectionB[i].style.display = "none";
   }
}

function hide_section_C(){
    // show div based on incoterms
    var sectionC = document.getElementsByClassName("sectionC");
    for(let i = 0 ; i<sectionC.length;i++){
    sectionC[i].style.display = "none";
   }
}

function hide_section_D(){
    // show div based on incoterms
    var sectionD = document.getElementsByClassName("sectionD");
    for(let i = 0 ; i<sectionD.length;i++){
    sectionD[i].style.display = "none";
   }
}

function hide_section_E(){
    // show div based on incoterms
    var sectionE = document.getElementsByClassName("sectionE");
    for(let i = 0 ; i<sectionE.length;i++){
    sectionE[i].style.display = "none";
   }
}


    // hide all form elements
    // function hide_all(){
    //     var mainform = document.getElementsByClassName("main-form");

    //     document.getElementById("").style.display = "block";
    // }
    // hide_all();

   //hide sections based on type of shipment 
//     var type_of_shipment = document.getElementById("quotation-form").onchange = function(){
//     var type = document.getElementById("id_type").value;
//     alert(type);
//     var getallclasses = document.getElementsByClassName("form-control");

//     for (let i = 0; i < getallclasses.length; i++) {
//         getallclasses[i].style.display = "none";
//     }

//     if(type == "sea"){
//         alert("Sea Shipment");
//     }
//     else if(type == "air"){
//         alert("Air Shipment");
//     }
//     else{
//         alert("Land Shipment");
//     }
// }
// alert(type_of_shipment);