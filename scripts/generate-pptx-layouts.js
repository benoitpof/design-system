const pptxgen = require("pptxgenjs");
const fs = require("fs");

const C = {
  navy:  "1C1F3B", teal:  "80C7C2", coral: "E8546C",
  steel: "435D74", light: "F9FCFF", mid:   "EAEBED",
  gray6: "6C757D", white: "FFFFFF", body:  "1C1F3B", navy2: "05387B",
};
const F = { h: "Poppins", b: "Raleway" };

function imgB64(path) {
  const data = fs.readFileSync(path);
  return "image/jpeg;base64," + data.toString("base64");
}
const IMG = {
  tech:  imgB64("/mnt/user-data/uploads/24_11_21_INSTALLATION_ET_MISE_EN_ROUTE_MU_P1256368_Mae_va_Bardy_-_Plastic_Odyssey.jpg"),
  cdf_d: imgB64("/mnt/user-data/uploads/24_11_21_INSTALLATION_ET_MISE_EN_ROUTE_MU_P1257016_Mae_va_Bardy_-_Plastic_Odyssey.jpg"),
  cdf_n: imgB64("/mnt/user-data/uploads/IMG_4238_-_Grande.jpeg"),
  solar: imgB64("/mnt/user-data/uploads/Usine.JPG"),
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title  = "POF — Layout Showcase v1";

// ── shared helpers ──────────────────────────────────────────────────────────
const makeShadow = () => ({ type: "outer", blur: 8, offset: 3, angle: 135, color: "000000", opacity: 0.12 });

function hdr(slide, title, sub) {
  slide.addText(title.toUpperCase(), {
    x:0.748, y:0.75, w:15, h:0.48,
    fontFace:F.h, fontSize:22, bold:true, color:C.teal, charSpacing:1.5, margin:0,
  });
  if (sub) slide.addText(sub, {
    x:0.748, y:1.27, w:15, h:0.42,
    fontFace:F.b, fontSize:19, color:C.navy, margin:0,
  });
  slide.addShape(pres.shapes.RECTANGLE,{x:0.748,y:0.75,w:0.055,h:0.48,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  slide.addShape(pres.shapes.RECTANGLE,{x:0.25,y:0.25,w:0.16,h:0.16,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  slide.addShape(pres.shapes.RECTANGLE,{x:19.59,y:10.84,w:0.16,h:0.16,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  slide.addText("PLASTIC ODYSSEY\nFACTORIES.",{x:16.2,y:0.62,w:3.55,h:0.72,fontFace:F.h,fontSize:8.5,bold:true,color:C.navy,align:"right",margin:0});
}
function hdrDark(slide,title,sub){
  hdr(slide,title,sub);
  // Override logo white
  slide.addText("PLASTIC ODYSSEY\nFACTORIES.",{x:16.2,y:0.62,w:3.55,h:0.72,fontFace:F.h,fontSize:8.5,bold:true,color:C.white,align:"right",margin:0});
}
function lbl(slide, id) {
  slide.addText(id,{x:0.4,y:10.82,w:5,h:0.28,fontFace:F.b,fontSize:9,color:C.gray6});
}

// ══ L01 COVER ══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.navy};
  s.addImage({data:IMG.cdf_n, x:8.5,y:0,w:11.5,h:11.25, sizing:{type:"cover",w:11.5,h:11.25}});
  s.addShape(pres.shapes.RECTANGLE,{x:8.5,y:0,w:11.5,h:11.25,fill:{color:C.navy,transparency:42},line:{color:C.navy,transparency:100}});
  // wave deco
  for(let i=0;i<3;i++) s.addShape(pres.shapes.RECTANGLE,{x:0,y:8.8+i*0.55,w:7.5-i*1.5,h:0.11,fill:{color:C.teal,transparency:i*28},line:{color:C.teal,transparency:100}});
  s.addShape(pres.shapes.RECTANGLE,{x:0.25,y:0.25,w:0.16,h:0.16,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  s.addShape(pres.shapes.RECTANGLE,{x:19.59,y:10.84,w:0.16,h:0.16,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  s.addText("PITCH DECK · 2025",{x:0.748,y:1.8,w:7.5,h:0.45,fontFace:F.h,fontSize:13,bold:true,color:C.teal,charSpacing:3,margin:0});
  s.addText("Transforming\nWaste into\nLocal Wealth.",{x:0.748,y:2.4,w:7.8,h:3.8,fontFace:F.h,fontSize:42,bold:true,color:C.white,lineSpacingMultiple:1.15,margin:0});
  s.addText("200 containerized recycling factories\nacross West Africa, Indian Ocean &\nSoutheast Asia by 2030.",{x:0.748,y:6.55,w:7.5,h:1.5,fontFace:F.b,fontSize:18,color:C.white,margin:0,lineSpacingMultiple:1.4});
  s.addText("April 2025",{x:0.748,y:8.3,w:4,h:0.4,fontFace:F.b,fontSize:15,color:C.gray6,margin:0});
  s.addText("PLASTIC ODYSSEY\nFACTORIES.",{x:16.2,y:0.62,w:3.55,h:0.72,fontFace:F.h,fontSize:8.5,bold:true,color:C.white,align:"right",margin:0});
  lbl(s,"L01 · COVER");
}

// ══ L02 SECTION DIVIDER ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.navy};
  s.addImage({data:IMG.cdf_d, x:0,y:0,w:20,h:11.25, sizing:{type:"cover",w:20,h:11.25}});
  s.addShape(pres.shapes.RECTANGLE,{x:0,y:0,w:20,h:11.25,fill:{color:C.navy,transparency:28},line:{color:C.navy,transparency:100}});
  s.addText("01",{x:11.5,y:0.3,w:8,h:5.5,fontFace:F.h,fontSize:170,bold:true,color:C.teal,transparency:78,align:"right",margin:0});
  s.addShape(pres.shapes.RECTANGLE,{x:0.25,y:0.25,w:0.16,h:0.16,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  s.addText("SECTION 01",{x:0.748,y:3.5,w:9,h:0.55,fontFace:F.h,fontSize:13,bold:true,color:C.teal,charSpacing:4,margin:0});
  s.addText("The Problem",{x:0.748,y:4.2,w:11,h:1.6,fontFace:F.h,fontSize:50,bold:true,color:C.white,margin:0});
  s.addText("80% of ocean plastic originates from land-based\nsources in low- and middle-income countries.",{x:0.748,y:6.1,w:9.5,h:1.3,fontFace:F.b,fontSize:19,color:C.white,margin:0,lineSpacingMultiple:1.4});
  s.addShape(pres.shapes.RECTANGLE,{x:0,y:10.88,w:20,h:0.37,fill:{color:C.teal,transparency:32},line:{color:C.teal,transparency:100}});
  s.addText("PLASTIC ODYSSEY\nFACTORIES.",{x:16.2,y:0.62,w:3.55,h:0.72,fontFace:F.h,fontSize:8.5,bold:true,color:C.white,align:"right",margin:0});
  lbl(s,"L02 · SECTION DIVIDER");
}

// ══ L03 CONTENT + IMAGE ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.white};
  hdr(s,"The CDF — Containerized Recycling Unit","A turnkey factory deployable in 72 hours");
  s.addText("What's inside a CDF?",{x:0.748,y:2.1,w:8.8,h:0.55,fontFace:F.h,fontSize:21,bold:true,color:C.navy,margin:0});
  const bl = [
    "Industrial-grade extruder optimized for HDPE, PP and mixed plastics",
    "Sorting and washing station pre-integrated",
    "Locally repairable — no specialized technicians required",
    "Processes up to 1,000 tonnes of plastic per year",
    "Solar-ready: compatible with off-grid energy setup",
    "Blockchain traceability via Inclusiv app on every batch",
  ];
  s.addText(bl.map(b=>({text:b,options:{bullet:true,breakLine:true}})),{
    x:0.748,y:2.75,w:8.8,h:8.0,fontFace:F.b,fontSize:18,color:C.body,paraSpaceAfter:8,lineSpacingMultiple:1.25,valign:"top",
  });
  s.addImage({data:IMG.tech, x:9.9,y:0,w:10.1,h:11.25, sizing:{type:"cover",w:10.1,h:11.25}});
  lbl(s,"L03 · CONTENT + IMAGE");
}

// ══ L04 BIG NUMBERS ════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.white};
  hdr(s,"Impact Per Factory","Measured, verifiable, and local");
  s.addImage({data:IMG.cdf_d, x:0.748,y:2.05,w:5.9,h:8.0, sizing:{type:"cover",w:5.9,h:8.0}});
  const stats=[
    {num:"1,000T",unit:"PLASTIC / YEAR",lbl:"diverted from landfill and ocean"},
    {num:"30",unit:"FORMAL JOBS",lbl:"created per factory at full capacity"},
    {num:"1",unit:"FACTORY",lbl:"serves a city of 30,000 people"},
  ];
  stats.forEach((st,i)=>{
    const y = 2.05 + i * 2.72;
    const dark = i===1;
    s.addShape(pres.shapes.RECTANGLE,{x:7.3,y,w:11.45,h:2.58,fill:{color:dark?C.navy2:C.navy},line:{color:C.navy,transparency:100}});
    s.addText(st.num,{x:7.6,y:y+0.12,w:6.8,h:1.4,fontFace:F.h,fontSize:60,bold:true,color:C.teal,margin:0,valign:"bottom"});
    s.addText(st.unit,{x:7.6,y:y+1.5,w:10.8,h:0.45,fontFace:F.h,fontSize:15,bold:true,color:C.white,charSpacing:1.5,margin:0});
    s.addText(st.lbl,{x:7.6,y:y+2.05,w:10.8,h:0.38,fontFace:F.b,fontSize:15,color:C.teal,margin:0});
  });
  lbl(s,"L04 · BIG NUMBERS");
}

// ══ L05 VALUE PROP (3 cards) ═══════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.white};
  hdr(s,"What We Provide","A complete franchise package — not just machines");
  const cards=[
    {icon:"⚙",title:"Machines & Technology",body:"Field-tested containerized units optimized for HDPE, PP, and mixed plastics. Locally repairable with standard tools."},
    {icon:"🎓",title:"Training & Support",body:"On-site commissioning, AI-assisted digital playbooks, ongoing remote technical assistance throughout operations."},
    {icon:"🌍",title:"Market Access",body:"Structured offtake agreements. Impact Plastic brand. Blockchain traceability via the Inclusiv app on every kilogram."},
  ];
  const cW=5.8, cH=7.5, gap=0.3, sx=0.748;
  // Total: 0.748 + 3*5.8 + 2*0.3 = 0.748+17.4+0.6 = 18.748" — fits safely
  cards.forEach((c,i)=>{
    const x = sx + i*(cW+gap);
    const y = 2.0;
    s.addShape(pres.shapes.RECTANGLE,{x,y,w:cW,h:cH,fill:{color:C.light},line:{color:C.mid,pt:0.5},shadow:makeShadow()});
    s.addShape(pres.shapes.RECTANGLE,{x,y,w:cW,h:0.22,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
    s.addShape(pres.shapes.OVAL,{x:x+0.28,y:y+0.4,w:0.88,h:0.88,fill:{color:C.navy},line:{color:C.navy,transparency:100}});
    s.addText(c.icon,{x:x+0.28,y:y+0.4,w:0.88,h:0.88,fontFace:F.b,fontSize:24,align:"center",valign:"middle",margin:0});
    s.addText(c.title,{x:x+0.28,y:y+1.45,w:cW-0.45,h:0.88,fontFace:F.h,fontSize:18,bold:true,color:C.navy,margin:0,lineSpacingMultiple:1.2});
    s.addText(c.body,{x:x+0.28,y:y+2.42,w:cW-0.45,h:4.8,fontFace:F.b,fontSize:16,color:C.body,margin:0,lineSpacingMultiple:1.4,valign:"top"});
  });
  lbl(s,"L05 · VALUE PROPOSITION");
}

// ══ L06 PROCESS FLOW ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.white};
  hdr(s,"Franchise Deployment","From signed contract to operational factory in under 6 months");
  const steps=[
    {n:"01",t:"Feasibility Study",b:"Site assessment, market sizing, offtake validation"},
    {n:"02",t:"Financing Setup",b:"Leasing structure, DFI grants, local bank coordination"},
    {n:"03",t:"CDF Delivery",b:"Manufacturing in Dakar, shipping, customs clearance"},
    {n:"04",t:"Installation",b:"72h deployment, on-site training, commissioning"},
    {n:"05",t:"Operations",b:"Ongoing support, remote monitoring, offtake management"},
  ];
  const sW=3.5, cy=5.5, sx=0.3;
  s.addShape(pres.shapes.LINE,{x:sx+0.5,y:cy,w:sW*5-0.3,h:0,line:{color:C.navy,pt:1.5}});
  steps.forEach((st,i)=>{
    const cx = sx + i*sW + sW/2;
    s.addShape(pres.shapes.OVAL,{x:cx-0.52,y:cy-0.52,w:1.04,h:1.04,fill:{color:C.navy},line:{color:C.teal,pt:2}});
    s.addText(st.n,{x:cx-0.52,y:cy-0.52,w:1.04,h:1.04,fontFace:F.h,fontSize:16,bold:true,color:C.teal,align:"center",valign:"middle",margin:0});
    s.addText(st.t,{x:cx-1.5,y:cy-2.55,w:3.0,h:0.9,fontFace:F.h,fontSize:13,bold:true,color:C.navy,align:"center",margin:0,lineSpacingMultiple:1.2});
    s.addShape(pres.shapes.LINE,{x:cx,y:cy-1.65,w:0,h:1.13,line:{color:C.teal,pt:1,dashType:"dash"}});
    s.addText(st.b,{x:cx-1.5,y:cy+0.7,w:3.0,h:2.3,fontFace:F.b,fontSize:13,color:C.gray6,align:"center",margin:0,lineSpacingMultiple:1.3});
  });
  lbl(s,"L06 · PROCESS FLOW");
}

// ══ L07 BAR CHART ══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.white};
  hdr(s,"Revenue Projections 2025–2030","Consolidated network across 3 regional clusters");
  s.addChart(pres.charts.BAR,[
    {name:"Equipment Sales (€M)",  labels:["2025","2026","2027","2028","2029","2030"],values:[1.2,3.5,7.8,14.2,22.0,34.0]},
    {name:"Services & Support (€M)",labels:["2025","2026","2027","2028","2029","2030"],values:[0.3,1.1,2.8,5.5,9.2,15.0]},
    {name:"Impact Credits (€M)",   labels:["2025","2026","2027","2028","2029","2030"],values:[0.0,0.2,0.8,2.0,4.5,9.0]},
  ],{
    x:0.748,y:1.95,w:14.0,h:8.2,
    barDir:"col", barGrouping:"stacked",
    chartColors:[C.navy,C.steel,C.teal],
    chartArea:{fill:{color:C.white}},
    valGridLine:{color:C.mid,size:0.5}, catGridLine:{style:"none"},
    catAxisLabelColor:C.gray6, valAxisLabelColor:C.gray6,
    showLegend:true, legendPos:"b", legendFontSize:12,
    showTitle:false,
  });
  // Stat callout
  s.addShape(pres.shapes.RECTANGLE,{x:15.3,y:1.95,w:3.95,h:3.0,fill:{color:C.navy},line:{color:C.navy,transparency:100},shadow:makeShadow()});
  s.addText("€58M",{x:15.3,y:2.15,w:3.95,h:1.4,fontFace:F.h,fontSize:42,bold:true,color:C.teal,align:"center",margin:0});
  s.addText("target revenue\nby 2030",{x:15.3,y:3.55,w:3.95,h:1.0,fontFace:F.b,fontSize:15,color:C.white,align:"center",margin:0,lineSpacingMultiple:1.3});
  s.addText("* Projections based on 200 factories target — illustrative",{x:0.748,y:10.5,w:13.5,h:0.38,fontFace:F.b,fontSize:12,color:C.gray6,italic:true,margin:0});
  lbl(s,"L07 · BAR CHART");
}

// ══ L08 TABLE ══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.white};
  hdr(s,"Franchise Package Comparison","CDF Standard · CDF Pro · PTF Industrial");
  const data=[
    [""             ,"CDF STANDARD" ,"CDF PRO"         ,"PTF INDUSTRIAL"],
    ["Capacity"     ,"300T / year"  ,"600T / year"     ,"1,200T / year"],
    ["CAPEX"        ,"€120–160K"    ,"€200–280K"       ,"€450–600K"],
    ["Jobs created" ,"10–15"        ,"20–25"           ,"30–50"],
    ["Financing"    ,"Leasing 5Y"   ,"Leasing + grant" ,"DFI + equity"],
    ["Payback"      ,"18–24 months" ,"24–36 months"    ,"36–48 months"],
    ["Training"     ,"2 weeks"      ,"4 weeks"         ,"8 weeks + Academy"],
  ];
  const td = data.map((row,ri)=>row.map((cell,ci)=>({
    text:cell,
    options:{
      fontFace:ci===0&&ri>0?F.h:(ri===0?F.h:F.b),
      fontSize:16,
      bold:ri===0||ci===0,
      color:ri===0?C.white:ci===0?C.navy:C.body,
      align:ci===0?"left":"center",
      fill:ri===0?{color:C.navy}:ci===0?{color:C.light}:ri%2===0?{color:C.white}:{color:C.light},
      valign:"middle",
      margin:[5,8,5,8],
    }
  })));
  s.addTable(td,{x:0.748,y:2.0,w:18.2,rowH:0.94,border:{pt:0},colW:[3.0,5.07,5.07,5.06]});
  lbl(s,"L08 · TABLE");
}

// ══ L09 SWOT ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.white};
  hdr(s,"Strategic Analysis","SWOT — Plastic Odyssey Factories");
  const qs=[
    {lt:"S",lb:"STRENGTHS",  bg:C.navy, tc:C.white, x:0.748, y:2.05,
     items:["Proprietary CDF — proven in 10+ countries","Franchise model reduces deployment risk","AFD institutional partnership + DFI pipeline","In-house manufacturing hub in Dakar"]},
    {lt:"W",lb:"WEAKNESSES", bg:C.light,tc:C.navy,  x:9.87, y:2.05,
     items:["High upfront CAPEX vs NGO models","Limited brand awareness outside West Africa","Dependency on local offtake market maturity"]},
    {lt:"O",lb:"OPPORTUNITIES",bg:C.teal,tc:C.navy, x:0.748,y:6.7,
     items:["EPR legislation accelerating in target markets","Virgin polymer prices surging → recycled premium","€5Bn+ DFI capital targeting plastic sector","Indian Ocean & SE Asia expansion via ER Group"]},
    {lt:"T",lb:"THREATS",    bg:C.mid,  tc:C.navy,  x:9.87, y:6.7,
     items:["Hormuz crisis → freight cost volatility","Political instability in key markets","NGO-funded units undercutting on pricing"]},
  ];
  const qW=8.8, qH=4.35;
  qs.forEach(q=>{
    s.addShape(pres.shapes.RECTANGLE,{x:q.x,y:q.y,w:qW,h:qH,fill:{color:q.bg},line:{color:C.mid,pt:0.5}});
    s.addText(q.lt,{x:q.x+qW-1.9,y:q.y+0.05,w:1.7,h:1.7,fontFace:F.h,fontSize:88,bold:true,color:q.bg===C.navy?C.teal:C.navy,transparency:78,align:"right",margin:0});
    s.addText(q.lb,{x:q.x+0.3,y:q.y+0.18,w:qW-0.55,h:0.42,fontFace:F.h,fontSize:13,bold:true,color:q.tc,charSpacing:1.5,margin:0});
    s.addText(q.items.map(it=>({text:it,options:{bullet:true,breakLine:true}})),{
      x:q.x+0.3,y:q.y+0.75,w:qW-0.55,h:qH-1.0,fontFace:F.b,fontSize:15,color:q.tc,paraSpaceAfter:5,lineSpacingMultiple:1.3,margin:0,
    });
  });
  s.addShape(pres.shapes.RECTANGLE,{x:9.12,y:6.01,w:1.77,h:0.64,fill:{color:C.white},line:{color:C.teal,pt:1.5}});
  s.addText("SWOT",{x:9.12,y:6.01,w:1.77,h:0.64,fontFace:F.h,fontSize:14,bold:true,color:C.navy,align:"center",valign:"middle",margin:0});
  lbl(s,"L09 · SWOT");
}

// ══ L10 CALLOUT DARK ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = {color:C.navy};
  s.addImage({data:IMG.solar, x:0,y:0,w:20,h:11.25, sizing:{type:"cover",w:20,h:11.25}});
  s.addShape(pres.shapes.RECTANGLE,{x:0,y:0,w:20,h:11.25,fill:{color:C.navy,transparency:32},line:{color:C.navy,transparency:100}});
  for(let i=0;i<3;i++) s.addShape(pres.shapes.RECTANGLE,{x:0,y:8.65+i*0.52,w:8.5-i*2,h:0.12,fill:{color:C.teal,transparency:i*30},line:{color:C.teal,transparency:100}});
  s.addShape(pres.shapes.RECTANGLE,{x:0.25,y:0.25,w:0.16,h:0.16,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  s.addShape(pres.shapes.RECTANGLE,{x:19.59,y:10.84,w:0.16,h:0.16,fill:{color:C.teal},line:{color:C.teal,transparency:100}});
  s.addText("OUR VISION",{x:1.2,y:2.4,w:14,h:0.55,fontFace:F.h,fontSize:15,bold:true,color:C.teal,charSpacing:4,margin:0});
  s.addText("Plastic Odyssey Factories bridges\nimpact and profitability —\ntransforming local waste into local wealth.",{
    x:1.2,y:3.1,w:14.5,h:4.2,fontFace:F.h,fontSize:38,bold:true,color:C.white,lineSpacingMultiple:1.22,margin:0,
  });
  s.addText("200 factories · 10,000 jobs · 200,000T plastic diverted annually by 2030",{x:1.2,y:7.6,w:14,h:0.65,fontFace:F.b,fontSize:19,color:C.teal,margin:0});
  s.addShape(pres.shapes.RECTANGLE,{x:1.2,y:8.75,w:5.8,h:0.88,fill:{color:C.teal},line:{color:C.teal,transparency:100},shadow:makeShadow()});
  s.addText("Join the network →",{x:1.2,y:8.75,w:5.8,h:0.88,fontFace:F.h,fontSize:18,bold:true,color:C.navy,align:"center",valign:"middle",margin:0});
  s.addText("PLASTIC ODYSSEY\nFACTORIES.",{x:16.2,y:0.62,w:3.55,h:0.72,fontFace:F.h,fontSize:8.5,bold:true,color:C.white,align:"right",margin:0});
  lbl(s,"L10 · CALLOUT DARK");
}

pres.writeFile({fileName:"/home/claude/pof-layouts.pptx"})
  .then(()=>console.log("✅ Done"))
  .catch(e=>{console.error("❌",e);process.exit(1);});
