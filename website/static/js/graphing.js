function graph() {

    $.get("/lineargraphdata", function(data, status) {

        var arr = eval(data.replace(/\s/g, ''));

        const result = regression.linear(arr);
        const gradient = result.equation[0];
        const yIntercept = result.equation[1];

        $("#r2_score").text(result.r2.toString());

        const useful_points = result.points.map(([x, y]) => {
            return {
                x,
                y
            };
        });

        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    datasets: [{
                        type: 'scatter',
                        label: 'Average Line',
                        borderColor: 'rgba(54, 162, 235, .8)',
                        backgroundColor: 'rgba(54, 162, 235, .8)',
                        data: useful_points,
                        labels: ['x', 'y'],
                        showLine: true,
                        pointRadius: 0,
                        pointHitRadius: 0,
                    }, {
                        type: 'scatter',
                        label: 'Sale Price',
                        borderColor: 'rgba(255, 0, 0, 0.2)',
                        backgroundColor: 'rgba(255, 0, 0, 0.3)',
                        data: arr,
                        labels: ['x', 'y']
                    }],
                    options: {

                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            x: {
                                type: 'linear',
                                position: 'bottom'
                            },
                            y: {
                                type: 'linear'
                            }
                        }
                    }
                }
            }

        )
    });

    $.get("/mvgraphdata", function(data, status) {
        $("#mvl_score").text(data);

    });


};