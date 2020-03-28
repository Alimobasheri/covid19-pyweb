const ChartColumns = columns =>
	columns.reduce((titles, title, idx) =>
		`${titles}<td key='${idx}'>
			${title}
		</td>`
	,'')

const ChartRows = rows => 
	rows.reduce((accrows, row, ridx) =>
		accrows+`<tr key=${ridx}>`+
			row.reduce((items, item, itidx) =>
				`${items}<td key=${itidx}>${item}</td>`
			,'')
		+'</tr>'
	,'')

const Chart = (title, date, columns, rows) => 
	`<h1 class='chart-title'>${title}</h1>
	<span class='chart-date'>${date.day}/${date.month}/${date.year}</span>
	<table class='chart'>
		<thead>
			${ChartColumns(columns)}
		</thead>
		<tbody>
			${ChartRows(rows)}
		</tbody>
	</table>`
