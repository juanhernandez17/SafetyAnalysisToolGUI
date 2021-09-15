

$(document).ready(function () {
    var csrftoken = getCookie('csrftoken');
    //form_handler()
    get_systems()
    form_update()
    form_add()
    form_del()
})
var csrftoken = getCookie('csrftoken');
// Get EnvEntity

function get_envstates(json, id) {
    $("#li-env-states").empty()
    for (var i = 0; i < json.entities[id].states.length; i++) {
        console.log(json[i])
        $("#li-env-states").append('<div class="list-group-item list-group-item-action" id="list-' + json.entities[id].states[i].id + '" data-toggle="list" aria-controls="' + i + '">' + json.entities[id].states[i].name + "</div>");
    }
    $('#li-env-states div').on('click', function (e) {
        e.preventDefault()
        var o = $(this).attr('aria-controls')

        $('#formt').text('Editing Env ' + json.entities[id].states[o].name)

        //----
        $('#FormControlInput1').val(json.entities[id].states[o].name); 
        $('#FormControlTextarea1').val(json.entities[id].states[o].description); 
        $('#parent').val(json.entities[id].states[o].Environmental_Entity)
        $("#num").val(json.entities[id].states[o].id)
        $('#system').val(json.entities[id].System)
        $("#type").val("entitys")
        
        //----
    })
}

function get_envprops(json, id) {
    $("#li-env-prop").empty()
    for (var i = 0; i < json.entities[id].properties.length; i++) {
        console.log(json[i])
        $("#li-env-prop").append('<div class="list-group-item list-group-item-action" id="list-' + json.entities[id].properties[i].id + '" data-toggle="list" aria-controls="' + i + '">' + json.entities[id].properties[i].name + "</div>");
    }
    $('#li-env-prop div').on('click', function (e) {
        e.preventDefault()
        var o = $(this).attr('aria-controls')

        $('#formt').text('Editing Env ' + json.entities[id].properties[o].name)

        //----
        $('#FormControlInput1').val(json.entities[id].properties[o].name); 
        $('#FormControlTextarea1').val(json.entities[id].properties[o].description); 
        $('#parent').val(json.entities[id].properties[o].Environmental_Entity)
        $("#num").val(json.entities[id].properties[o].id)
        $('#system').val(json.entities[id].System)
        $("#type").val("entityp")
        //----
    })
}

// Get Components
function get_componentstates(json, id) {
    $("#li-coms").empty()
    for (var i = 0; i < json.components[id].states.length; i++) {
        console.log(json[i])
        $("#li-coms").append('<div class="list-group-item list-group-item-action" id="list-' + json.components[id].states[i].id + '" data-toggle="list" aria-controls="' + i + '">' + json.components[id].states[i].name + "</div>");
    }
    $('#li-coms div').on('click', function (e) {
        e.preventDefault()
        var o = $(this).attr('aria-controls')

        $('#formt').text('Editing Comp ' + json.components[id].states[o].name)
        $('#FormControlInput1').val(json.components[id].states[o].name); 
        $('#FormControlTextarea1').val(json.components[id].states[o].description); 
        $('#parent').val(json.components[id].states[o].Component)
        $("#num").val(json.components[id].states[o].id)
        $('#system').val(json.components[id].System)
        $("#type").val("components")
    

    })
}

function get_componentprops(json, id) {
    $("#li-comp").empty()
    for (var i = 0; i < json.components[id].properties.length; i++) {
        console.log(json[i])
        $("#li-comp").append('<div class="list-group-item list-group-item-action" id="list-' + json.components[id].properties[i].id + '" data-toggle="list" aria-controls="' + i + '">' + json.components[id].properties[i].name + "</div>");
    }
    $('#li-comp div').on('click', function (e) {
        e.preventDefault()
        var o = $(this).attr('aria-controls')

        $('#formt').text('Editing Comp ' + json.components[id].properties[o].name)
        $('#FormControlInput1').val(json.components[id].properties[o].name); 
        $('#FormControlTextarea1').val(json.components[id].properties[o].description); 
        $('#parent').val(json.components[id].properties[o].Component)
        $("#num").val(json.components[id].properties[o].id)
        $('#system').val(json.components[id].System)
        $("#type").val("componentp")
    
})
}
// get system info components and entities
function get_compent(json) {
    $("#li-com").empty()
   
    for (var i = 0; i < json.components.length; i++) {
        $("#li-com").append('<div class="list-group-item list-group-item-action" id="list-' + json.components[i].id + '" data-toggle="list" aria-controls="' + i + '">' + json.components[i].name + "</div>");
    }
    
    $('#li-com div').on('click', function (e) {
        e.preventDefault()
        var id = $(this).attr('aria-controls')

        $('#formt').text('Editing ' + json.components[id].name)
        $('#FormControlInput1').val(json.components[id].name); 
        $('#FormControlTextarea1').val(json.components[id].description); 
        $('#system').val(json.components[id].System)
        $("#num").val(json.components[id].id)
        $("#type").val("component")
        $('#parent').val(json.components[id].id)
        get_componentstates(json, id)
        get_componentprops(json, id)
        
      
        
    })
    
    $("#li-env-ent").empty()
    for (var i = 0; i < json.entities.length; i++) {
        $("#li-env-ent").append('<div class="list-group-item list-group-item-action" id="list-' + json.entities[i].id + '" data-toggle="list" aria-controls="' + i + '">' + json.entities[i].name + "</div>");
    }
   
    $('#li-env-ent div').on('click', function (e) {
        e.preventDefault()
        var id = $(this).attr('aria-controls')
        get_envstates(json, id)
        get_envprops(json, id)
        $('#formt').text('Editing ' + json.entities[id].name)
        $('#FormControlInput1').val(json.entities[id].name)
        $('#FormControlTextarea1').val(json.entities[id].description)
        $('#system').val(json.entities[id].System)
        $("#num").val(json.entities[id].id)
        $("#type").val("entity")
        $('#parent').val(json.entities[id].id)



    })
   
};

// Get List of Systems
function get_systems() {
    var ur = "/api/systems.json"
    $.ajax({
        url: ur, // the endpoint
        type: "GET", // http method
        // handle a successful response
        success: function (json) {
            for (var i = 0; i < json.length; i++) {
                $("#li-sys").append('<div class="list-group-item list-group-item-action" id="list-' + json[i].id + '" data-toggle="list" aria-controls="' + i + '">' + json[i].name + "</div>");
            }
            $('#li-sys div').on('click', function (e) {
                e.preventDefault()
                var id = $(this).attr('id').replace('list-', '')
                var i = $(this).attr('aria-controls')
                $('#formt').text('Editing ' + json[i].name)
                $('#FormControlInput1').val(json[i].name); 
                $('#FormControlTextarea1').val(json[i].description); 
                $('#system').val(id)
                get_system(id)

            })
        },
        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function get_system(id) {
    var url = "/api/system/full/" + id + ".json"
    $.ajax({
        url: url, // the endpoint
        type: "GET", // http method
        // handle a successful response
        success: function (json) {
            $("#li-env-states").empty()
            $("#li-env-prop").empty()
            $("#li-env-ent").empty()
            $("#li-com").empty()
            $("#li-coms").empty()
            $("#li-comp").empty()
            get_compent(json)
        },
        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

// Update name and description for selected element
function form_update(){
    
      
    $("#sub").on('click',function(e){
        e.preventDefault()

        var  type = document.getElementById("type").value
        var  id = document.getElementById("num").value
         if( type === "component" || type === "entity")
        {
            var url= "/api/"+type+"/RUD/"+id
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  System = document.getElementById("system").value
            fetch(url,{
                method:'PUT',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'System':System})
                
            }
            ).then(function(response){
                get_system(System)
             })
        } else if(type==='components'||type==='componentp'){
            var url= "/api/"+type+"/RUD/"+id
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  Component = document.getElementById("parent").value
            var  System = document.getElementById("system").value
            fetch(url,{
                method:'PUT',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'Component':Component})
                
            }
            ).then(function(response){
                get_system(System)
            })
        }else if(type==='entitys'||type==='entityp'){
            
            var url= "/api/"+type+"/RUD/"+id
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  Environmental_Entity = document.getElementById("parent").value
            var  System = document.getElementById("system").value
            
            fetch(url,{
                method:'PUT',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'Environmental_Entity':Environmental_Entity})
                
            }
            ).then(function(response){
               get_system(System)
            })
    
    
        } else if(type==="comp_add"){

            var url= "/api/component/create/"
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  System = document.getElementById("system").value
            fetch(url,{
                method:'POST',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'System':System})
                
            }
            ).then(function(response){
                 get_system(System)
                 document.getElementById('my_form').reset()
                
            })
        
        
        
        }else if(type==="env_add"){

            var url= "/api/entity/create/"
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  System = document.getElementById("system").value
            fetch(url,{
                method:'POST',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'System':System})
                
            }
            ).then(function(response){
                
                get_system(System)
                document.getElementById('my_form').reset()
                
            })
        
        
        
        }else if(type==="comps_add" || type=="compp_add"){

            if (type=="comps_add") {var url= "/api/components/create/"}
            else if(type="compp_add"){var url= "/api/componentp/create/"}
            
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  System = document.getElementById("system").value
            var  Component = document.getElementById("parent").value
            fetch(url,{
                method:'POST',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'Component':Component})
                
            }
            ).then(function(response){
                get_system(System)
                document.getElementById('my_form').reset()
                
            })
        
         }else if(type==="envs_add" || type=="envp_add"){

            if (type=="envs_add") {var url= "/api/entitys/create/"}
            else if(type="envp_add"){var url= "/api/entityp/create/"}
            
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  System = document.getElementById("system").value
            var  Environmental_Entity = document.getElementById("parent").value
            console.log(System)
            fetch(url,{
                method:'POST',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'Environmental_Entity':Environmental_Entity})
                
            }
            ).then(function(response){
                
                get_system(System)
                document.getElementById('my_form').reset()
                
            })
        
         }
       
    
    });
        
   
}
//add new element to the system 
function form_add(){
    $("#comp_but").on('click',function(e){
        e.preventDefault()
        document.getElementById('my_form').reset()
        $("#type").val("comp_add")
        $('#formt').text('Editing New Comp ')
    });
    $("#env_but").on('click',function(e){
        e.preventDefault()
        document.getElementById('my_form').reset()
        $("#type").val("env_add")
        $('#formt').text('Editing New ENV ')
    });
     $("#comps_but").on('click',function(e){
        e.preventDefault()
        document.getElementById('my_form').reset()
        $("#type").val("comps_add")
        $('#formt').text('Editing New C State ')
    });
    $("#compp_but").on('click',function(e){
        e.preventDefault()
        document.getElementById('my_form').reset()
        $("#type").val("compp_add")

        $('#formt').text('Editing New Comp Prop ')
    });
    $("#envs_but").on('click',function(e){
        e.preventDefault()
        document.getElementById('my_form').reset()
        $("#type").val("envs_add")
        $('#formt').text('Editing New Env State ')
    });
    $("#envp_but").on('click',function(e){
        e.preventDefault()
        document.getElementById('my_form').reset()
        $("#type").val("envp_add")

        $('#formt').text('Editing New Env Prop ')
    });
}
//Function to delete elements
function form_del()
{
    $("#del").on('click',function(e){
        e.preventDefault()
        var  type = document.getElementById("type").value
        var  id = document.getElementById("num").value
        if( type === "component" || type === "entity")
        {
            var url= "/api/"+type+"/RUD/"+id
            var  System = document.getElementById("system").value
            fetch(url,{
                method:'DELETE',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                
                
            }
            ).then(function(response){
                get_system(System)
                document.getElementById('my_form').reset()
                
            })
        }else if(type==='components'||type==='componentp'){
           
            var url= "/api/"+type+"/RUD/"+id
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  Component = document.getElementById("parent").value
            var  System = document.getElementById("system").value
            fetch(url,{
                method:'DELETE',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'Component':Component})
                
            }
            ).then(function(response){
                get_system(System)
                document.getElementById('my_form').reset()
            })
        }else if(type==='entitys'||type==='entityp'){
            
            var url= "/api/"+type+"/RUD/"+id
            var  name = document.getElementById("FormControlInput1").value
            var  description = document.getElementById("FormControlTextarea1").value
            var  Environmental_Entity = document.getElementById("parent").value
            var  System = document.getElementById("system").value
            
            fetch(url,{
                method:'DELETE',
                headers:{
                    'Content-type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'name':name,'description':description,'Environmental_Entity':Environmental_Entity})
                
            }
            ).then(function(response){
                get_system(System)
                document.getElementById('my_form').reset()
            })
    
    
        } 

    })
    
}

//---------------------
  // using jQuery to get csrftoken
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }