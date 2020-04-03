const ChartColumns = columns =>
	'<td> ID</td>'+columns.reduce((titles, title, idx) =>
		`${titles}<td key='${idx}' class='chart-head-td'>
			${title}
		</td>`
	,'')

const ChartRows = rows => 
	rows.reduce((accrows, row, ridx) =>
		accrows+`<tr key=${ridx}><td>${ridx+1}</td>`+
			row.reduce((items, item, itidx) =>
				`${items}<td key=${itidx} class='chart-body-td'>${item}</td>`
			,'')
		+'</tr>'
	,'')

const Chart = (title, date, columns, rows) => 
	`
	<div class='chart-wrapper'>
		<div class='chart-title-date-wrapper'>
			<h1 class='chart-title'>${title}</h1>
			<span class='chart-date'>${date.day}/${date.month}/${date.year}</span>
		</div>
		<table class='chart-table'>
			<thead class='chart-head'>
				<tr class='chart-head-row'>
					${ChartColumns(columns)}
				</tr>
			</thead>
			<tbody class='chart-body'>
				${ChartRows(rows)}
			</tbody>
		</table>
	</div>`
