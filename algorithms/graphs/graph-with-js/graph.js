const airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM YYZ ICN'.split(' ');

const routes = [
    ['PHX', 'LAX'],
    ['PHX', 'JFK'],
    ['JFK', 'OKC'],
    ['JFK', 'HEL'],
    ['JFK', 'LOS'],
    ['MEX', 'LAX'],
    ['MEX', 'BKK'],
    ['MEX', 'LIM'],
    ['MEX', 'EZE'],
    ['LIM', 'BKK'],
];

// adj list is better option (not many '1's will fill a matrix)

// map works better in most cases when dealing with adj lists
const adjList = new Map();

function addNode(airport) {
    adjList.set(airport, []);
}

// adding undirected edge 
function addEdge(origin, destination) {
    adjList.get(origin).push(destination);
    adjList.get(destination).push(origin);
}

// Now create the graph

airports.forEach(addNode);
routes.forEach(route => addEdge(...route));

console.log(adjList);


// BFS !
function bfs(start, target) {
    const visited = new Set();
    const que = [start]
    
    while (que.length > 0) {
        const airport = que.shift(); // mutating op

        const destinations = adjList.get(airport);
        
        for (const dest of destinations) {
            if (dest === target) {
                console.log(`found it in ${visited.size} steps`)
                console.log(...visited)
            }
            if (!visited.has(dest)) {
                visited.add(dest);
                que.push(dest);
            }
        }        
    }    
}

// DFS !
function dfs(start, visited = new Set()) {
    console.log(start)

    visited.add(start)

    const destinations = adjList.get(start)

    for (const dest of destinations) {
        if (dest === "BKK") {
            console.log(`DFS has found Bangkok in ${visited.size} steps`)
            return
        }

        if (!visited.has(dest)) {
            dfs(dest, visited)
        }
    }
}