var w = window.innerWidth,
    h = window.innerHeight,
    fill = d3.scale.category20();

var nodeSize = 20;
var charge = -960;
var linkDistance = 120;

var vis = d3.select("#chart")
  .append("svg:svg")
    .attr("width", w)
    .attr("height", h);

d3.json("/json", function(json) {
  var force = d3.layout.force()
      .charge(charge)
      .linkDistance(linkDistance)
      .nodes(json.nodes)
      .links(json.links)
      .size([w, h])
      .start();

  var link = vis.selectAll("line.link")
      .data(json.links)
    .enter().append("svg:line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return 10; })
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; })
      .attr("source", function(d) { return d.source.name; })
      .attr("target", function(d) { return d.target.name; });

  link.append("svg:title")
    .text(function(d) { 
      return d.source.name.concat(" --> ", d.target.name);
    })

  var node = vis.selectAll("circle.node")
      .data(json.nodes)
    .enter().append("svg:circle")
      .attr("class", "node")
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; })
      .attr("r", nodeSize)
      .attr("name", function(d) { return d.name })
      .attr("selected", false)
      .style("fill", function(d) { return fill(d.group); })
      .on("click", nodeClick)
      .call(force.drag);

  node.append("svg:title")
    .text(function(d) { return d.name; })

  vis.style("opacity", 1e-6)
    .transition()
      .duration(1000)
      .style("opacity", 1);

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; })

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  });

  d3.select("svg").append("text")
    .attr('id', 'title')
    .attr("x", w/2)             
    .attr("y", 200)
    .attr("text-anchor", "middle")  
    .style("font-size", "10em") 
    .text(json.package_name);


  function selectNode(name) {
    var selector = "[name=%s]".replace('%s', name)
                              .replace(/\./g, '\\.');
    var node = d3.select(selector);
    return node;
  }

  function selectLinks(node, type) {
    var selector = "[%s=%s]".replace('%s', type)
                            .replace("%s", node)
                            .replace(/\./g, '\\.');
    var links = d3.selectAll(selector);
    return links;
  }

  function unhighlightNode(name) {
    var node = selectNode(name);
    node.transition().duration(500)
      .attr("r", nodeSize)
      .style("fill", function(d) { return fill(d.group); });

    var imports = selectLinks(name, 'source');
    imports.transition().duration(500)
      .style("stroke", "");

    var imports = selectLinks(name, 'target');
    imports.transition().duration(500)
      .style("stroke", "");
  }

  function highlightNode(name) {
    var node = selectNode(name);
    node.transition().duration(500)
      .attr("r", nodeSize * 2)
      .style("fill", "red");

    var imports = selectLinks(name, 'source');
    imports.transition().duration(500)
      .style("stroke", "red");

    var imports = selectLinks(name, 'target');
    imports.transition().duration(500)
      .style("stroke", function(d) { return fill(d.group); });
  }

  function nodeClick() {
    var name = d3.select(this).attr('name');
    var previous_name = d3.select("#title").text();

    if (name === previous_name) {
      d3.select(this).attr("selected", false);
      d3.select("#title").text(json.package_name);
      unhighlightNode(name)
    } else {
      d3.select(this).attr("selected", true);
      d3.select("#title").text(name);
      unhighlightNode(previous_name);
      highlightNode(name);
    }
  }
});
