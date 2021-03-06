function rook(n) 
{
    if (n === 0) return [];
    if (n === 1) return [[[1]]];

    var solutions = [];
    var sol = rook(n-1);
    for (var i = 0; i < sol.length; i++) {
        solutions = solutions.concat(appendrook(sol[i]));
    }
    return solutions;
}

function appendrook(sol)
{
    var n = sol.length + 1;
    var newset=[];
    var newrow=Array.apply(null, new Array(n-1)).map(Number.prototype.valueOf,0);
    newrow.push(1);
    for (var i=0; i<n; i++){
        var newarr = [];
        for (var j = 0; j < n-1; j++) {
            var row = sol[j];
            newarr.push(row.slice(0).concat(0)); //append empty square to every row
        }
        newarr.splice(i,0, newrow); //insert new rook ending row
        newset.push(newarr);
    }
    return newset;
}


var sol=rook(3);
console.log(sol.length);
console.log(sol);
