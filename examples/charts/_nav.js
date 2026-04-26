// Shared topbar navigation script for all chart pages
const CHART_LIST=[['01','01-kpi.html','KPI'],['02','02-bar.html','Bar'],['03','03-stacked.html','Stacked'],['04','04-grouped.html','Grouped'],['05','05-line.html','Line'],['06','06-donut.html','Donut'],['07','07-progress.html','Progress'],['08','08-funnel.html','Funnel'],['09','09-timeline.html','Timeline'],['10','10-gantt.html','Gantt'],['11','11-sankey.html','Sankey'],['12','12-process.html','Process'],['13','13-org.html','Org'],['14','14-table.html','Table'],['15','15-radar.html','Radar'],['16','16-map.html','Map']];
(()=>{
const here=(location.pathname.split('/').pop()||'').toLowerCase();
const nav=document.getElementById('types-nav');
if(!nav) return;
CHART_LIST.forEach(([n,f,l])=>{const a=document.createElement('a');a.href=f;a.textContent=l;a.title=l;if(f===here)a.classList.add('active');nav.appendChild(a)});
})();
