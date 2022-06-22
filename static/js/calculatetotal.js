
//make fields readonly
$('#id_margin_origin_haulage,#id_margin_customs_documentation,#id_margin_origin_terminal_handling,\
#id_margin_port_charges,#id_margin_other_charges,#id_margin_freight_cost,\
#id_margin_other_freight_charges,#id_margin_total_origin,#id_margin_terminal_handling,\
#id_margin_port_charges_dest,#id_margin_agency_fee,#id_margin_transport_delivery,\
#id_margin_other_destination_charges,#id_total_tax,#id_grand_total,\
#id_buying_total_origin,#id_selling_total_origin,\
#id_buying_total_destination,#id_selling_total_destination,\
#id_margin_total_destination,#id_sub_total_duties,#id_sub_total_taxes').attr('readonly', true);

//calculate margins
$('.numberinput').on('change',function(){
  var pressed = this;
  var pressed_id = pressed.id;
  var bp_amt = 0;
  var sp_amt = 0;
  var margin_amt = 0;

  if(pressed_id.includes("buying")){
      //get selling price value
      let getsp = document.getElementById(pressed_id.replace("buying","selling"));
      let getsp_amt = getsp.value;

      bp_amt = pressed.value;
      margin_amt = getsp_amt - bp_amt;
      let replace_id = document.getElementById(pressed_id.replace("buying","margin"));
      replace_id.value = margin_amt;
      
  }
  else if(pressed_id.includes("selling")){
      let getbp = document.getElementById(pressed_id.replace("selling","buying"));
      let getbp_amt = getbp.value;

      sp_amt = pressed.value;
      margin_amt = sp_amt - getbp_amt;
      let replace_id = document.getElementById(pressed_id.replace("selling","margin"));
      replace_id.value = margin_amt;
  }

  })

  //calculate totals origins buying rate
  $('.numberinput').on('change',function(){
    var buying_origin = Number(document.getElementById("id_buying_origin_haulage").value);
    var buying_customs = Number(document.getElementById("id_buying_customs_documentation").value);
    var buying_origin_terminal = Number(document.getElementById("id_buying_origin_terminal_handling").value);
    var buying_port_charges = Number(document.getElementById("id_buying_port_charges").value);
    var buying_other_charges = Number(document.getElementById("id_buying_other_charges").value);
    var buying_freight_charges = Number(document.getElementById("id_buying_freight_cost").value);
    var buying_other_freight_charges = Number(document.getElementById("id_buying_other_freight_charges").value);

    var totals_buying_rate = buying_origin + buying_customs + buying_origin_terminal +
    buying_port_charges + buying_other_charges + buying_freight_charges + 
    buying_other_freight_charges;

    document.getElementById("id_buying_total_origin").value = totals_buying_rate;
  })

  //calculate totals origins selling rate
  $('.numberinput').on('change',function(){
    var selling_origin = Number(document.getElementById("id_selling_origin_haulage").value);
    var selling_customs = Number(document.getElementById("id_selling_customs_documentation").value);
    var selling_origin_terminal = Number(document.getElementById("id_selling_origin_terminal_handling").value);
    var selling_port_charges = Number(document.getElementById("id_selling_port_charges").value);
    var selling_other_charges = Number(document.getElementById("id_selling_other_charges").value);
    var selling_freight_charges = Number(document.getElementById("id_selling_freight_cost").value);
    var selling_other_freight_charges = Number(document.getElementById("id_selling_other_freight_charges").value);

    var totals_selling_rate = selling_origin + selling_customs + selling_origin_terminal +
    selling_port_charges + selling_other_charges + selling_freight_charges + 
    selling_other_freight_charges;

    document.getElementById("id_selling_total_origin").value = totals_selling_rate;
  })

  //calculate totals origins margin rate
  $('.numberinput').on('change',function(){
    var margin_origin = Number(document.getElementById("id_margin_origin_haulage").value);
    var margin_customs = Number(document.getElementById("id_margin_customs_documentation").value);
    var margin_origin_terminal = Number(document.getElementById("id_margin_origin_terminal_handling").value);
    var margin_port_charges = Number(document.getElementById("id_margin_port_charges").value);
    var margin_other_charges = Number(document.getElementById("id_margin_other_charges").value);
    var margin_freight_charges = Number(document.getElementById("id_margin_freight_cost").value);
    var margin_other_freight_charges = Number(document.getElementById("id_margin_other_freight_charges").value);

    var totals_margin_rate = margin_origin + margin_customs + margin_origin_terminal +
    margin_port_charges + margin_other_charges + margin_freight_charges + 
    margin_other_freight_charges;

    document.getElementById("id_margin_total_origin").value = totals_margin_rate;
  })

  //calculate totals destination buying rate
  $('.numberinput').on('change',function(){
    var buying_terminal = Number(document.getElementById("id_buying_terminal_handling").value);
    var buying_port = Number(document.getElementById("id_buying_port_charges_dest").value);
    var buying_agency_fee = Number(document.getElementById("id_buying_agency_fee").value);
    var buying_transport = Number(document.getElementById("id_buying_transport_delivery").value);
    var buying_destination = Number(document.getElementById("id_buying_other_destination_charges").value);
    
    var totals_buying_rate = buying_terminal + buying_port + buying_agency_fee +
    buying_transport + buying_destination;

    document.getElementById("id_buying_total_destination").value = totals_buying_rate;
  })

  //calculate totals destination selling rate
  $('.numberinput').on('change',function(){
    var selling_terminal = Number(document.getElementById("id_selling_terminal_handling").value);
    var selling_port = Number(document.getElementById("id_selling_port_charges_dest").value);
    var selling_agency_fee = Number(document.getElementById("id_selling_agency_fee").value);
    var selling_transport = Number(document.getElementById("id_selling_transport_delivery").value);
    var selling_destination = Number(document.getElementById("id_selling_other_destination_charges").value);
    
    var totals_selling_rate = selling_terminal + selling_port + selling_agency_fee +
    selling_transport + selling_destination;

    document.getElementById("id_selling_total_destination").value = totals_selling_rate;
  })

  //calculate totals destination margin rate
  $('.numberinput').on('change',function(){
    var margin_terminal = Number(document.getElementById("id_margin_terminal_handling").value);
    var margin_port = Number(document.getElementById("id_margin_port_charges_dest").value);
    var margin_agency_fee = Number(document.getElementById("id_margin_agency_fee").value);
    var margin_transport = Number(document.getElementById("id_margin_transport_delivery").value);
    var margin_destination = Number(document.getElementById("id_margin_other_destination_charges").value);
    
    var totals_margin_rate = margin_terminal + margin_port + margin_agency_fee +
    margin_transport + margin_destination;

    document.getElementById("id_margin_total_destination").value = totals_margin_rate;
  })

  //calculate totals import duties
  $('.numberinput').on('change',function(){
    var hs_code = Number(document.getElementById("id_hs_code").value);
    var fob_value = Number(document.getElementById("id_fob_value").value);
    var freight_charges = Number(document.getElementById("id_freight_charges").value);
    var insurance = Number(document.getElementById("id_insurance").value);
    var customs_value = Number(document.getElementById("id_customs_value").value);
    
    var totals_duties = hs_code + fob_value + freight_charges +
    insurance + customs_value;

    document.getElementById("id_sub_total_duties").value = totals_duties;
  })

  //calculate taxes
  $('.numberinput').on('change',function(){
    var import_duty = Number(document.getElementById("id_import_duty").value);
    var excise_duty = Number(document.getElementById("id_excise_duty").value);
    var vat = Number(document.getElementById("id_vat").value);
    var railway_levy = Number(document.getElementById("id_railway_levy").value);
    var idf_fee = Number(document.getElementById("id_idf_fee").value);
    var levies = Number(document.getElementById("id_levies").value);
    
    var totals_tax = import_duty + excise_duty + vat +
    railway_levy + idf_fee + levies;

    document.getElementById("id_sub_total_taxes").value = totals_tax;
  })

    //calculate total taxes
    $('.numberinput').on('change',function(){
        
        var duties = Number(document.getElementById("id_sub_total_duties").value);
        var tax = Number(document.getElementById("id_sub_total_taxes").value);
        
        var totals_tax = duties + tax;
    
        document.getElementById("id_total_tax").value = totals_tax;
      })


    //calculate grand total
    $('.numberinput').on('change',function(){

      //total selling
      var selling_origin = Number(document.getElementById("id_selling_total_origin").value);
      var selling_destination = Number(document.getElementById("id_selling_total_destination").value);
      var total_tax = Number(document.getElementById("id_total_tax").value);
      
      
      //total selling
      var total_selling = selling_origin + selling_destination  + total_tax;
      
      document.getElementById("id_grand_total").value = total_selling;
      document.getElementById("id_grand_total").innerHTML = total_selling;
    })
    

    //incoterms
    var incoterms = document.getElementById("incoterms_id").value;
    console.log(incoterms);
    if(incoterms == "EX WORKS"){

    }
    else if(incoterms == "FOB"){
        hide_section_A();
    }
    else if(incoterms == "CRF"){
        hide_section_A();
        hide_section_B();
    }
    else if(incoterms == "DAP"){
        hide_section_D();
        hide_section_E();
    }

    function hide_section_A(){
        // show div based on incoterms
        var incoterms = document.getElementById("incoterms_id").value;
        var sectionA = document.getElementsByClassName("sectionA");
        for(let i = 0 ; i<sectionA.length;i++){
        sectionA[i].style.display = "none";
        console.log("TTTT");
       }
    }

    function hide_section_B(){
        // show div based on incoterms
        var incoterms = document.getElementById("incoterms_id").value;
        var sectionB = document.getElementsByClassName("sectionB");
        for(let i = 0 ; i<sectionB.length;i++){
        sectionB[i].style.display = "none";
       }
    }

    function hide_section_C(){
        // show div based on incoterms
        var incoterms = document.getElementById("incoterms_id").value;
        var sectionC = document.getElementsByClassName("sectionC");
        for(let i = 0 ; i<sectionC.length;i++){
        sectionC[i].style.display = "none";
       }
    }

    function hide_section_D(){
        // show div based on incoterms
        var incoterms = document.getElementById("incoterms_id").value;
        var sectionD = document.getElementsByClassName("sectionD");
        for(let i = 0 ; i<sectionD.length;i++){
        sectionD[i].style.display = "none";
       }
    }

    function hide_section_E(){
        // show div based on incoterms
        var incoterms = document.getElementById("incoterms_id").value;
        var sectionE = document.getElementsByClassName("sectionE");
        for(let i = 0 ; i<sectionE.length;i++){
        sectionE[i].style.display = "none";
       }
    }