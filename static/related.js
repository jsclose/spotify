$(function () {
   
	$("#get_network").click(get_related_artist);

/*
	$("#get_network").on('click', function(){
		$artist_name = $("#artist").val();
		get_related_artist(artist_name);

	});
*/

});




function get_related_artist(artist_name){
	$artist_name = $("#artist").val();
	

    $.ajax({
        url: "/api/v1/related_artist",
        type: 'GET',
        contentType: "application/json",
        data: {artist_name : $artist_name},
        dataType: 'json',
        //data : JSON.stringify(),
        success: function (data) {
        	
            console.log("Pass");
            console.log(data);

            display_network(data);
            //need way to remeber most recent url
           
           

        },
        error: function (data) {
            console.log(data);

        }
    });


};





function display_network(json){

    //Remove preivous SVG
    svg.selectAll("*").remove()
        /* Draw the node labels first */


        var texts = svg.selectAll("text")
            .data(json.nodes)
            .enter()
                .append("text")
                .attr("fill", "black")
                .attr("font-family", "sans-serif")
                .attr("font-size", "10px")
                .text(function(d) {
                    return d.id;
                });
        /* Establish the dynamic force behavor of the nodes */
        var force = d3.layout.force()
            .nodes(json.nodes)
            .links(json.links)
            .size([w, h])
            .linkDistance([10])
            .charge([-750])
            .gravity(0.4)
            .start();
        /* Draw the edges/links between the nodes */
        var edges = svg.selectAll("line")
            .data(json.links)
            .enter()
            .append("line")
            .style("stroke", "#ccc")
            .style("stroke-width", 1)
            .attr("marker-end", "url(#end)");
        /* Draw the nodes themselves */
        var nodes = svg.selectAll("circle")
            .data(json.nodes)
            .enter()
            .append("circle")
            .attr("r", function(d){
                return Math.sqrt(d.followers/10000)
            })
            .attr("opacity", 0.5)
            .style("fill", function(d, i) {
               return color(i)
            })
            .call(force.drag)
             .on('dblclick', connectedNodes); //Added code 
        /* Run the Force effect */
        force.on("tick", function() {
            edges.attr("x1", function(d) {
                    return d.source.x;
                })
                .attr("y1", function(d) {
                    return d.source.y;
                })
                .attr("x2", function(d) {
                    return d.target.x;
                })
                .attr("y2", function(d) {
                    return d.target.y;
                });
            nodes.attr("cx", function(d) {
                    return d.x;
                })
                .attr("cy", function(d) {
                    return d.y;
                })
            texts.attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
            });
        });


//Toggle stores whether the highlighting is on
var toggle = 0;
//Create an array logging what is connected to what
var linkedByIndex = {};
for (i = 0; i < json.nodes.length; i++) {
    linkedByIndex[i + "," + i] = 1;
};
json.links.forEach(function (d) {
    linkedByIndex[d.source.index + "," + d.target.index] = 1;
});
//This function looks up whether a pair are neighbours
function neighboring(a, b) {
    return linkedByIndex[a.index + "," + b.index];
}
function connectedNodes() {
    if (toggle == 0) {
        //Reduce the opacity of all but the neighbouring nodes
        d = d3.select(this).node().__data__;
        nodes.style("opacity", function (o) {
            return neighboring(d, o) | neighboring(o, d) ? 1 : 0.1;
        });
        edges.style("opacity", function (o) {
            return d.index==o.source.index | d.index==o.target.index ? 1 : 0.1;
        });
        edges.style("stroke-width", function (o) {
            return d.index==o.source.index | d.index==o.target.index ? 3 : 0.8;
        });

        
        //Reduce the op
        toggle = 1;
    } else {
        //Put them back to opacity=1
        nodes.style("opacity", .5);
        edges.style("opacity", 1);

        toggle = 0;
    }
}

};









