
window.onload = function() {
    
    var btn_clear = document.getElementById('btn_clear');

    btn_clear.onclick = function(){
        document.getElementById('search').innerHTML = "";
        document.getElementById('result').innerHTML = "";
        showHint();
    }

    // $(".example").hide();

    // var btn_show = document.getElementByClassName('btn_li');
    // btn_show.onclick = function(){
    //     $(this).next().slideToggle(200);
    // }
    
}

// $(document).ready(function(){


// });

$(document).ready(function() {
  $("#search span").on("mouseenter", function () {
    $("#search span").attr( "tooltip_visible", "true" );
  }).on("mouseleave", function () {
    $("#search span").attr( "tooltip_visible", "false" );
  });
});

// $(document).ready(function() {
//   $(".example").hide();
//   $(".btn_li").click(function() {
//      $(this).next().slideToggle(200);
//   });
//   $(".example").slideUp(200);
// });

function showTooltip(w1, w2, w3, hover){
  $( "#search span" ).last().attr( "tooltip_visible", "true" );
  $( "#search span" ).last().attr( "tooltip", w1+" "+w2+" "+w3 );
  $( "#search span" ).last().attr( "flow", "down" );
  $( "#search span" ).last().attr( "data-balloon-length", "fit" );
}

last = "";
spanned = true;
function _showHint(str, hover) {
  if (str.length == 0) {
    str = last
  } else {
    last = str = str.replace(/(\s+)|(&nbsp;)/g," ");
  }

  xmlHttp=new XMLHttpRequest();
  var tmpstr = str.split(' ').slice(-10).join(' ')
  if (hover != undefined) {
    var url="add?text=" + tmpstr + "&hover=" + hover;
  } else {
    var url="add?text=" + tmpstr;
  }

  xmlHttp.open("GET", url, true);
  xmlHttp.send();

  xmlHttp.onreadystatechange = function() {
    //console.log('yeah!, I\'m half and half success!!')
    if(xmlHttp.readyState==4) {
      var str = xmlHttp.responseText;
      str = str.substring(1, str.length-1);
      var tmpp = str.split('+++');
      var spelltmp = tmpp[1].split('^');
      //spell
      var tmp = tmpp[0].split('+'); // seperate each pat
      // document.getElementById('result').innerHTML = "";
      var ans = "";
      for(var i in tmp){
          s = tmp[i].split('_'); // seperate pat and each example
          if(typeof s !== 'undefined' && s.length > 0){
            var percentage = s[0].split('(');
              ans += ('<li class="list-group-item " style="text-align: left;"><span><div style="display: block;">'+percentage[0]+'</div>');
            
              if (typeof percentage[1] !== 'undefined'){   
                 ans += ('<div class="progress" style="margin-top: 10px;"><span style="display: block;width: '+ percentage[1] + ' " class="progress-bar-striped bg-info" role="progressbar">'+percentage[1]+'</span></div></span><ul class="list-group">');
              }

              for(var j=1; j<=4; j++){
                if(s.length>j){
                  if(j==4){
                    sstmp = s[j].split('=====');
                    ans += ('<li class="list-group-item result_node" onclick="itemClicked(event)">'+sstmp[0]+'</li>');
                    ans += ('<li class="list-group-item example_node"><button class="btn btn-secondary btn-lg btn_li" onclick="btnClicked(event)">show example</button><div class="example">'+sstmp[1].substring(2, sstmp[1].length-2)+'</div></li>'); //sent
                  }
                  else{
                    ans += ('<li class="list-group-item result_node" onclick="itemClicked(event)">'+s[j]+'</li>');
                  }
                }
              }
              
              ans += ('</ul></li>');
          }
      }
      document.getElementById('result').innerHTML = ans;
      showTooltip(spelltmp[0], spelltmp[1], spelltmp[2], hover);
    }
  }


}
function searchText() {
  if ($("#search")[0].innerText == undefined) {
    return $("#search")[0].innerHTML.replace(/<br>/gi,"\n").replace(/(<([^>]+)>)/g, "").replace(/&nbsp;/g," ");
  } else {
    return $("#search")[0].innerText;
  }
}
function showHint(hover) {
  _showHint(searchText(), hover);
}
function getIndex(node) {
  i = 0;
  while( (node = node.previousSibling) != null ) i++;
  return i
}
function spanText(event) {
  spanned = true;
  var str = searchText()
  if (str.slice(-1) == '\n') {
    str = str.substring(0, str.length - 1)
  }
  $("#search")[0].innerHTML = "<span>" + str.replace(/[\xa0 ]*\n/g," <br>").split(/[\xa0\ ]/g).join("</span><span>&nbsp;") + "</span>";
  setCaretLast();
  $("#search span").mouseenter(onHover);
  $("#search span").mouseleave(function(){
    $("#search span").attr( "tooltip_visible", "false" );
  })
}
function setCaretLast() {
    var el = $("#search")[0]
    var range = document.createRange();
    var sel = window.getSelection();
    range.setStartAfter(el.childNodes[el.childNodes.length-1]);
    range.collapse(true);
    sel.removeAllRanges();
    sel.addRange(range);
    el.focus();
}
function onHover(e) {
  node = e.currentTarget;
  //showHint(getIndex(node));
  showHint(node.innerHTML)
  $("#search span").attr( "tooltip_visible", "true" );
}
function onKey(e) {
  if($("#search")[0].innerText == "\n") {
    $("#search")[0].innerHTML = "";
  }
  str = searchText();
  if (!(str.length==0 || str == last)) {
    spanned = false;
    showHint();
  }
}
function onMouse(e) {
  if (!spanned && $("#search").text().length > 0) {
    spanText(e);
  }
}

function itemClicked(e) {
  var s = $("#search").text();
  // var input = document.getElementById('search');
  // var out = getCaretPosition(input);
  tmp = ' '
  if (/\s/.test(s[s.length-1])){
    tmp = ''
  }
  s += (tmp + e.currentTarget.innerHTML);
  // var tmp = s.substring(0, out.start) + e.currentTarget.innerHTML + s.substring(out.start, out.end);
  $("#search").html(s);
  showHint();
  spanned = false;
  spanText(e);

  // var l = tmp.length;
  // setCaretPosition(document.getElementById('search'), l, l);
}

  
function btnClicked(e){
  // $(this).next(".example").slideToggle(200);
  // $(".example").hide();
  $(this).next().slideToggle(200);
  // $(this).click(function() {
  //    $(this).next().slideToggle(200);
  //    // $(".example").show();

  //    // if($('.btn_li').next().css('display')=='none'){
  //    //   $('.btn_li').next().show();
  //    // }
  //    // else{
  //    //   $('.btn_li').next().hide();
  //    // }
  // });
  // $(this).unbind("click");
  // $(this).next().slideUp(200);
}

function btnClicked(e){
  // $(this).next(".example").slideToggle(200);
  // $(".example").hide();
  // $(this).next().slideToggle(200);
  $(this).click(function() {
     // $(this).next().slideToggle(200);
     // $(".example").show();

     if($('.btn_li').next().css('display')=='none'){
       $('.btn_li').next().show();
     }
     else{
       $('.btn_li').next().hide();
     }
  });
  // $(this).unbind("click");
  $(this).next().slideUp(200);
}
