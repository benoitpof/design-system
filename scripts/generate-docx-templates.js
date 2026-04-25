const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        Header, Footer, AlignmentType, LevelFormat,
        WidthType, ShadingType, PageNumber, BorderStyle, HeadingLevel } = require("docx");
const fs = require("fs");

const navy="1C1F3B", teal="80C7C2", light="F9FCFF", mid="EAEBED";
const gray6="6C757D", white="FFFFFF";
const A4W=11906, A4H=16838, M=1134;
const cW = A4W - 2*M; // 9638

const noB = { top:{style:BorderStyle.NONE,size:0}, bottom:{style:BorderStyle.NONE,size:0}, left:{style:BorderStyle.NONE,size:0}, right:{style:BorderStyle.NONE,size:0} };

const r = (text, {font="Raleway",size=22,color=navy,bold=false,italic=false}={}) =>
  new TextRun({text, font, size, color, bold, italics:italic});

const h = (text, opts={}) => r(text, {font:"Poppins",...opts});

const para = (children, {align=AlignmentType.LEFT, before=0, after=100}={}) =>
  new Paragraph({ alignment:align, spacing:{before, after}, children });

const spacer = (pt=200) => new Paragraph({ spacing:{before:pt, after:0}, children:[new TextRun({text:"",size:2})] });

const rule = (color=teal, size=6) => new Paragraph({
  border:{ bottom:{style:BorderStyle.SINGLE,size,color,space:1} },
  spacing:{before:80,after:80}, children:[new TextRun({text:"",size:2})]
});

const cell = (children, {fill=white,w=cW,mT=150,mB=150,mL=160,mR=160,borders=noB}={}) =>
  new TableCell({ width:{size:w,type:WidthType.DXA}, shading:{fill,type:ShadingType.CLEAR},
    margins:{top:mT,bottom:mB,left:mL,right:mR}, borders, children });

const row1 = (cellNode) => new Table({
  width:{size:A4W,type:WidthType.DXA}, columnWidths:[A4W],
  rows:[new TableRow({children:[cellNode]})]
});

// ══════════════════════════════════════════════════════════════════
// DOC 1 — COVER PAGE
// ══════════════════════════════════════════════════════════════════
const coverDoc = new Document({ sections:[{
  properties:{ page:{ size:{width:A4W,height:A4H}, margin:{top:0,right:0,bottom:0,left:0} } },
  children:[
    // ── Navy top block (2/3 height) ────────────────────────────
    row1(cell([
      spacer(800),
      para([h("RAPPORT D'IMPACT · 2025", {size:18,color:teal,bold:true})]),
      spacer(300),
      para([h("Transformer les\nDéchets en\nRichesse Locale.", {size:68,color:white,bold:true})], {before:0}),
      spacer(200),
      para([r("Plastic Odyssey Factories — Rapport Annuel 2025", {size:24,color:teal})]),
      spacer(600),
      rule(teal, 8),
      spacer(150),
      para([r("Dakar, Sénégal  ·  Avril 2025", {size:18,color:gray6})]),
      spacer(300),
    ],{fill:navy, w:A4W, mT:0, mB:0, mL:M, mR:M})),

    // ── Two-column bottom block ────────────────────────────────
    new Table({
      width:{size:A4W,type:WidthType.DXA},
      columnWidths:[Math.floor(A4W/2), Math.ceil(A4W/2)],
      rows:[new TableRow({children:[
        // Left: stats
        cell([
          para([h("Chiffres clés", {size:22,bold:true})]),
          rule(),
          ...[["10+","Pays déployés"],["30","Emplois formels / usine"],["1 000T","Plastique / an / usine"],["200","Usines cible d'ici 2030"]]
            .flatMap(([n,l])=>[
              spacer(100),
              para([h(n,{size:48,color:teal,bold:true})],{before:0}),
              para([r(l,{size:18})],{before:0,after:60}),
            ])
        ],{fill:light, w:Math.floor(A4W/2), mT:600, mB:600, mL:M, mR:300}),

        // Right: about + summary
        cell([
          para([h("À propos de POF", {size:22,bold:true})]),
          rule(),
          spacer(80),
          para([r("Plastic Odyssey Factories déploie des unités de recyclage conteneurisées dans les pays en développement via un modèle de franchise. Chaque usine crée des emplois locaux et traite jusqu'à 1 000 tonnes de plastique par an.", {size:19})],{before:0,after:160}),
          para([h("Sommaire", {size:22,bold:true})]),
          rule(),
          spacer(60),
          ...["01  Résumé exécutif","02  Vue réseau","03  Métriques d'impact","04  Performance financière","05  Perspectives 2026–2030"]
            .map(item => para([r(item,{size:19})],{before:60,after:60})),
        ],{fill:white, w:Math.ceil(A4W/2), mT:600, mB:600, mL:300, mR:M}),
      ]})]
    }),
  ]
}]});

// ══════════════════════════════════════════════════════════════════
// DOC 2 — BACK COVER
// ══════════════════════════════════════════════════════════════════
const backDoc = new Document({ sections:[{
  properties:{ page:{ size:{width:A4W,height:A4H}, margin:{top:0,right:0,bottom:0,left:0} } },
  children:[
    row1(cell([
      spacer(700),
      para([h("PLASTIC ODYSSEY\nFACTORIES.", {size:30,color:teal,bold:true})]),
      spacer(500),
      para([h("Clean up the past.\nBuild the future.", {size:52,color:white,bold:true})]),
      spacer(300),
      rule(teal,8),
      spacer(300),
      // 3-col contacts
      new Table({
        width:{size:cW,type:WidthType.DXA},
        columnWidths:[Math.floor(cW/3),Math.floor(cW/3),Math.ceil(cW/3)],
        rows:[new TableRow({children:[
          ...[
            {label:"Siège social",   lines:["Dakar, Sénégal","contact@pofactories.com","www.pofactories.com"]},
            {label:"Investisseurs",  lines:["Pierre Rousseau","investors@pofactories.com","+33 6 XX XX XX XX"]},
            {label:"Réseau franchise",lines:["Anna Kalifa","franchise@pofactories.com","po-factories.com"]},
          ].map(col => cell([
            para([h(col.label,{size:18,color:teal,bold:true})],{before:0,after:60}),
            ...col.lines.map(l=>para([r(l,{size:17,color:white})],{before:40,after:0})),
          ],{fill:navy, w:Math.floor(cW/3), mL:0, mR:180, mT:0, mB:0, borders:noB}))
        ]})]
      }),
      spacer(400),
      rule(teal,6),
      spacer(150),
      para([r("© 2025 Plastic Odyssey Factories SAS · Tous droits réservés", {size:15,color:gray6})]),
      spacer(100),
      para([r("Sustainable · Inclusive · Resilient · Profitable", {size:15,color:teal,italic:true})]),
      spacer(300),
    ],{fill:navy, w:A4W, mT:0, mB:0, mL:M, mR:M})),
  ]
}]});

// ══════════════════════════════════════════════════════════════════
// DOC 3 — BODY PAGE (page type rapport)
// ══════════════════════════════════════════════════════════════════
const bodyDoc = new Document({
  numbering:{config:[{
    reference:"bullets",
    levels:[{level:0, format:LevelFormat.BULLET, text:"·", alignment:AlignmentType.LEFT,
      style:{paragraph:{indent:{left:360,hanging:200}},
             run:{font:"Poppins",color:teal,size:22}}}]
  }]},
  styles:{
    default:{document:{run:{font:"Raleway",size:22,color:navy}}},
    paragraphStyles:[
      {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,
       run:{size:40,bold:true,font:"Poppins",color:navy},
       paragraph:{spacing:{before:480,after:120},outlineLevel:0}},
      {id:"Heading2",name:"Heading 2",basedOn:"Normal",next:"Normal",quickFormat:true,
       run:{size:28,bold:true,font:"Poppins",color:navy},
       paragraph:{spacing:{before:320,after:80},outlineLevel:1}},
      {id:"Heading3",name:"Heading 3",basedOn:"Normal",next:"Normal",quickFormat:true,
       run:{size:24,bold:true,font:"Poppins",color:"435D74"},
       paragraph:{spacing:{before:240,after:60},outlineLevel:2}},
    ]
  },
  sections:[{
    properties:{ page:{ size:{width:A4W,height:A4H}, margin:{top:M,right:M,bottom:M,left:M} } },
    headers:{ default: new Header({ children:[
      new Paragraph({
        border:{bottom:{style:BorderStyle.SINGLE,size:4,color:teal,space:4}},
        spacing:{before:0,after:160}, alignment:AlignmentType.LEFT,
        children:[h("PLASTIC ODYSSEY FACTORIES",{size:16,bold:true}), r("  ·  Rapport d'Impact 2025",{size:16,color:gray6})],
      })
    ]})},
    footers:{ default: new Footer({ children:[
      new Paragraph({
        border:{top:{style:BorderStyle.SINGLE,size:4,color:teal,space:4}},
        spacing:{before:100,after:0}, alignment:AlignmentType.RIGHT,
        children:[r("Page ",{size:16,color:gray6}), new TextRun({children:[PageNumber.CURRENT],font:"Raleway",size:16,color:gray6})],
      })
    ]})},
    children:[
      // H1 + rule
      new Paragraph({heading:HeadingLevel.HEADING_1,
        children:[new TextRun({text:"03 — Métriques d'Impact",font:"Poppins",bold:true,size:40,color:navy})]}),
      rule(teal,8),

      // H2
      new Paragraph({heading:HeadingLevel.HEADING_2,
        children:[new TextRun({text:"Détournement de plastique",font:"Poppins",bold:true,size:28,color:navy})]}),
      new Paragraph({spacing:{before:120,after:200}, children:[
        r("En 2024, les unités opérationnelles de Plastic Odyssey Factories ont collectivement détourné "),
        r("2 400 tonnes", {bold:true}),
        r(" de déchets plastiques de l'incinération et des océans. Cette performance représente une multiplication par 3,2 par rapport à 2023 et confirme la capacité du modèle franchise à se déployer sans compromettre la qualité ni la traçabilité."),
      ]}),

      // Bullets
      new Paragraph({spacing:{before:160,after:60}, children:[h("Résultats clés 2024 :",{size:22,bold:true})]}),
      ...["Granulés HDPE : 1 840T — vendus à 12 acheteurs industriels","Madriers plastiques PP : 340T — offtake municipal à Dakar et Abidjan","Palettes plastique mixte : 220T — programme pilote avec 3 entreprises FMCG"]
        .map(item => new Paragraph({numbering:{reference:"bullets",level:0}, spacing:{before:80,after:80}, children:[r(item)]})),

      spacer(160),

      // Callout block
      new Table({
        width:{size:cW,type:WidthType.DXA}, columnWidths:[180, cW-180],
        rows:[new TableRow({children:[
          cell([new Paragraph({children:[new TextRun({text:"",size:2})]})],
            {fill:teal, w:180, mT:0,mB:0,mL:0,mR:0,borders:noB}),
          cell([
            para([h("Point clé",{size:20,bold:true})],{before:0,after:60}),
            para([r("Chaque CDF opérationnel génère un ROI moyen de 22 % à l'année 2, d'après les données auditées 2024 sur 6 usines.",{size:20})],{before:0}),
          ],{fill:"F1FBFA", w:cW-180, mT:200,mB:200,mL:280,mR:160, borders:noB}),
        ]})]
      }),

      spacer(280),

      // H2
      new Paragraph({heading:HeadingLevel.HEADING_2,
        children:[new TextRun({text:"Emplois & Impact communautaire",font:"Poppins",bold:true,size:28,color:navy})]}),
      new Paragraph({spacing:{before:120,after:200}, children:[
        r("Chaque usine crée entre 10 et 30 emplois formels directs, et 3 à 5 fois plus dans l'écosystème informel de collecte. Le tableau ci-dessous résume les métriques d'emploi pour les déploiements actifs en 2024."),
      ]}),

      // Table
      new Table({
        width:{size:cW,type:WidthType.DXA},
        columnWidths:[2600,1900,1600,1600,1538],
        rows:[
          // Header
          new TableRow({children:[
            ...["Pays","Usine","Emplois directs","Emplois indirects","Statut"].map((h2,ci)=>
              new TableCell({
                width:{size:[2600,1900,1600,1600,1538][ci],type:WidthType.DXA},
                shading:{fill:navy,type:ShadingType.CLEAR},
                margins:{top:100,bottom:100,left:120,right:120},
                children:[new Paragraph({alignment:ci>0?AlignmentType.CENTER:AlignmentType.LEFT,
                  children:[new TextRun({text:h2,font:"Poppins",size:18,color:white,bold:true})]})]
              })
            )
          ]}),
          // Data
          ...[
            ["Sénégal","Dakar CDF-01","28","85","✓ Opérationnel"],
            ["Philippines","Cebu CDF-01","22","64","✓ Opérationnel"],
            ["Kenya","Mombasa CDF-01","18","52","✓ Opérationnel"],
            ["Côte d'Ivoire","Abidjan CDF-01","14","41","▶ Montée en charge"],
            ["Cameroun","Douala CDF-01","12","35","▶ Montée en charge"],
          ].map((row2,ri)=>new TableRow({children:[
            ...row2.map((c2,ci)=>new TableCell({
              width:{size:[2600,1900,1600,1600,1538][ci],type:WidthType.DXA},
              shading:{fill:ri%2===0?white:light,type:ShadingType.CLEAR},
              margins:{top:80,bottom:80,left:120,right:120},
              children:[new Paragraph({alignment:ci>0?AlignmentType.CENTER:AlignmentType.LEFT,
                children:[new TextRun({text:c2,font:ci===0?"Poppins":"Raleway",size:18,color:ci===0?navy:"3C3C3C",bold:ci===0})]})]
            }))
          ]}))
        ]
      }),

      spacer(160),
      new Paragraph({spacing:{before:0,after:0},
        children:[r("Source : POF Operations Database — Odoo v19 — Export avril 2025",{size:15,color:gray6,italic:true})]}),
    ]
  }]
});

Promise.all([
  Packer.toBuffer(coverDoc).then(b=>fs.writeFileSync("/home/claude/pof-doc-cover.docx",b)),
  Packer.toBuffer(backDoc).then(b=>fs.writeFileSync("/home/claude/pof-doc-backcover.docx",b)),
  Packer.toBuffer(bodyDoc).then(b=>fs.writeFileSync("/home/claude/pof-doc-body.docx",b)),
]).then(()=>console.log("✅ 3 DOCX written"))
  .catch(e=>{console.error("❌",e);process.exit(1);});
