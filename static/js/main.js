$(document).ready(function(){
    var dt = new Date();
    document.getElementById("date").innerHTML = "Last Update time : "+dt.toLocaleString();
    document.getElementById("date").style.textAlign = "right";
    document.getElementById("date").style.color = "white";

    document.getElementById("message").innerHTML = "System will auto update every 5 minute";
    document.getElementById("message").style.textAlign = "right";
    document.getElementById("message").style.color = "white";

    $('#sidebarCollapse').on('click', function () {
          $('#sidebar').toggleClass('active');
          $(this).toggleClass('active');
      });
    $.ajax({
      url:"https://rimsservicesqat.rimsrenalworks.com:8085/MA_Status/",
      //url:"http://localhost:8085/MA_Status/",
      contentType: "application/json",
      method: "GET",
      success: function(response){
          table_element(response);
          Dchart(response);
        },error:function(error){
          console.log("error")
          console.log(error)
        }
      })
  })

new Date().toLocaleString();
document.getElementById("date")
setTimeout(function () { 
    location.reload();
    }, 300 * 1000);
var xValues = ["Pass", "Fail"];
    var barColors = [
    "#00E396",
    "#f8bbd0"
    ];

function table_element(response){
    var table = document.getElementById('table_row');
    var table = '<h2 class="title3">MA Status</h2><table><tr class="row">'
    for (let i=0; i<response.length ;i++){
        
        table+='<td class = "chart-box"><div><h2 class="title2" id="MATitle"'+String(i)+'></h2><canvas id="myChart_MA"'+String(i)+' class="mainchart" ></canvas></div></td>'
        
    }
    table += +'</tr></table>'
}

function Dchart(response){
    for (let i=0; i<response.length ;i++){
    let chart = "myChart_MA" + String([i])
    
    if(response[i]['MA'].length !=0){
        var yValues_1 = [0,1];
    }
    else{
        var yValues_1 = [1,0];
    }

    new Chart(chart, {
        type: "doughnut",
        data: {
            labels: xValues,
            datasets: [{
            backgroundColor: barColors,
            data: yValues_1
            }]
        },
        options: {
            plugins:{
            title:{
                display: true,
                text: 'All MA Status',
                color: "White",
                font:{size:20,}
            },
            tooltip:{
                callbacks:{
                label:  function(){
                    if(response[i]['MA'].length !=0){
                        var matooltips = response[i]['MA']
                    }
                    else{
                        var matooltips = "All Pass"
                    }
                    return ``+matooltips+``
                } 
                },
                titleFontSize: 30,
                bodyFontSize: 30,
            },
            legend:{
                labels:{
                color:"White",
                font:{size:14}
                }
            },
            }
        }
        });
        }
        
        for (let i=0; i< response.length;i++){
        var HDtooltips = ""
        if(response[i]['Live_Data'].length !=0){
            var yValues_1 = [0,1];
        }
        else{
            var yValues_1 = [1,0];
        }
        let chart = "myChart_HD" + String([i])
        new Chart(chart, {
        type: "doughnut",
        data: {
            labels: xValues,
            datasets: [{
            backgroundColor: barColors,
            data: yValues_1
            }]
        },
        options: {
            plugins:{
            title:{
                display: true,
                text: 'All Live Data Status',
                color: "White",
                font:{size:20,}
            },
            tooltip:{
                callbacks:{
                label:  function(){
                    if(response[i]['Live_Data'].length !=0){
                        var HDtooltips = response[i]['Live_Data']
                    }
                    else{
                        var HDtooltips = "All Pass"
                    }
                    return ``+HDtooltips+``
                } 
                },
                titleFontSize: 30,
                bodyFontSize: 30,
            },
            legend:{
                labels:{
                color:"White",
                font:{size:14}
                }
            }
            }
        }
        });
        }
        for (let i=0; i< response.length;i++){
            if(response[i]['Network'] != "pass"){
                var yValues_1 = [0,1];
            }
            else{
                var NStooltips = "All Pass"
                var yValues_1 = [1,0];
            }
            let chart = "NS" + String([i])
            new Chart(chart, {
            type: "doughnut",
            data: {
                labels: xValues,
                datasets: [{
                backgroundColor: barColors,
                data: yValues_1
                }]
            },
            options: {
                plugins:{
                title:{
                    display: true,
                    text: 'Internet Status',
                    color: "White",
                    font:{size:20,}
                },
                tooltip:{
                    callbacks:{
                    label:  function(){
                        if(response[i]['Network'] != "pass"){
                            var NStooltips = "Network down"
                        }
                        else{
                            var NStooltips = "All Pass"
                        }
                        return ``+NStooltips+``
                    } 
                    },
                    titleFontSize: 30,
                    bodyFontSize: 30,
                },
                legend:{
                    labels:{
                    color:"White",
                    font:{size:14}
                    }
                }
                }
        }
        });
        }
    
    for (let i=0;i<=response.length;i++){
        if(response[i]['Branch'] == 'AVISENA'){
            response[i]['Branch'] = "Setia Alam"
        }
        document.getElementById("MATitle"+String(i)).innerHTML = response[i]['Branch'];
        document.getElementById("HDTtitle"+String(i)).innerHTML = response[i]['Branch'];
        document.getElementById("Network_Status"+String(i)).innerHTML = response[i]['Branch'];
        
    }
    
}
