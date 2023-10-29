
function main(crit) {
  let m=[],k;
 
  if(crit=="VanDerVarden" || crit=="Klotz" || crit=="Fisher" || crit=="Capon" || crit=="Ansari" || crit=="Mood" || crit=="Leman" || crit=="Wilcoxon"){
        k=2;
        m[0]=5;m[1]=7;
        range_go(crit,k,m);
  }
  if(crit=="Kruskal") {
        k=4;
        m[0]=3;m[1]=4;m[2]=4;m[3]=5;
        range_go(crit,k,m);
  }  
  if(crit=="Ansari-analitic") {
     let wrange=[],pw=[],nn;
     k=2;
     m[0]=5;m[1]=7;
     nn=data_ansari(m[0],m[1],wrange,pw)
     
     document.write(crit);
     document.write("<br>");
     document.write("Size="+nn);
     document.write("<br>");
     for (i=0;i<k;i++) document.write(m[i]+"  ");
     document.write("<br>");
     for (i=1;i<=nn;i++) {
        document.write(i+": "+wrange[i].toFixed(znaki)+"  "+pw[i].toFixed(znaki));
        document.write("<br>");  
     }
   }
   if(crit=="Wilcoxon-analitic") {
     let wrange=[],pw=[],nn;
     k=2;
     m[0]=5;m[1]=7;
     nn=wilcoxon(m[0],m[1],wrange,pw);
     document.write(crit);
     document.write("<br>");
     document.write("Size="+nn);
     document.write("<br>");
     for (i=0;i<k;i++) document.write(m[i]+"  ");
     document.write("<br>");
     for (i=1;i<=nn;i++) {
        document.write(i+": "+wrange[i].toFixed(znaki)+"  "+pw[i].toFixed(znaki));
        document.write("<br>");  
     }
   }
}