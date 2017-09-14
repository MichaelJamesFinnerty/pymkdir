function fnpress(json_string, dest) {        
    fnparse(new_fnobj("", json_string, 0, "", (dest ? dest : "")));
    return true;
}

function new_fnobj(fnref, _json, _i, _html, _dest) {
    
    var fnobj = {
        fnjson: (_json ? _json : (fnref.fnjson ? fnref.fnjson : "")),        
        indt: (_i ? _i : (fnref.indt ? fnref.indt : 0)),        
        html: (_html ? _html : (fnref.html ? fnref.html : 0)),        
        dest: (_dest ? _dest : (fnref.dest ? fnref.dest : "")),        
        insert_html: function() {
            this.html.style.marginLeft = detLeftMargin(this);
            if (!this.dest) {document.body.appendChild(this.html);
            } else {
                document.getElementById(this.dest).appendChild(this.html);
            }
        },
        mktml_h: function() {
            if (this.fnjson.slice(0,1) === "#") {
                this.indt = this.fnjson.slice(1,2);
                this.fnjson = this.fnjson.slice(2);
            } else if (this.fnjson.slice(0,1) === "*") {      
                var newHeading = document.createElement("h"+this.fnjson.slice(1,2));
                this.fnjson = this.fnjson.slice(2);                
            }

            if (!newHeading) {var newHeading = document.createElement("h"+this.indt);}  
            newHeading.className = "header"+this.indt;
            newHeading.innerHTML = this.fnjson;

            return newHeading;
        },        
        mktml_p: function() {

            if (this.fnjson.slice(0,2) === "#!") {        
                var newP = document.createElement("code");
                newP.className = "code";
                newP.innerHTML = this.fnjson.slice(2);

            } else {
                var newP = document.createElement("p");
                newP.className = "graf";
                newP.innerHTML = this.fnjson;        

            }
            
            return newP;
        },
        mktml_inj: function() {
                var newINJ = document.createElement("span");
                newINJ.insertAdjacentHTML('beforeend', this.fnjson)
            return newINJ;
        }        
    }
        
    function detLeftMargin(e){
      return eval(e.indt*12)+"px";
    };
            
    return fnobj;    
}


//build json into html contents
function fnparse(o) {
    
  //arrays
  if (Array.isArray(o.fnjson)) {
      
    //recurse each item back into fnparse
    for (f in o.fnjson) {
      var json_element = o.fnjson[f]
      fnparse(
          new_fnobj(o, json_element)
      );
    }

  //objects
  } else if (typeof(o.fnjson)==="object"){
    
    // each object level raises the indententation level by 1
    o.indt++;
      
    for (k in Object.keys(o.fnjson)) {
        
      var key = Object.keys(o.fnjson)[k];

      //console.log(Array(o.indt).join("\t"), key);
        
      // write the key as a heading element
      if (key.length > 3 || key[0] !== "#") {
        var newH = new_fnobj(o, key)
        newH.html = newH.mktml_h();
        newH.insert_html();
      }
   
      //fnparse the value paired with the key/heading
      var json_element = o.fnjson[key]
      if (json_element) {
        fnparse(
          new_fnobj(newH, json_element)
        );
      }
    }
      
  //strings;
  } else if (typeof(o.fnjson) === "string") {
      //insert string as graf
      if (o.fnjson.slice(0,1) != "<") {
        o.html = o.mktml_p();    
      } else {
        o.html = o.mktml_inj();
      }
      o.insert_html();
  } 

  return true;
};