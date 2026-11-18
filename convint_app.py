import uuid

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Convolution Integral",
    layout="wide",
)

# Remove Streamlit's default padding/header so the animation fills the page
st.markdown(
    """
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 1rem;}
    header[data-testid="stHeader"] {height: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

uid = "conv_" + uuid.uuid4().hex[:8]

html = r"""
<div id="ROOT_ID" class="animation-app">

<style>
#ROOT_ID {
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:clamp(8px, 2vw, 24px);
    box-sizing:border-box;
    font-family:Arial,sans-serif;
    position:relative;
    color:#1f2a44;
    background:linear-gradient(160deg,#f7f9ff 0%,#eaf0fc 100%);
    border-radius:18px;
    box-shadow:0 10px 30px rgba(31,42,68,0.10);
}

#ROOT_ID * { box-sizing:border-box; }

#ROOT_ID h2 {
    text-align:center;
    font-size:clamp(20px, 2.6vw, 30px);
    margin:12px 0 4px;
    letter-spacing:0.5px;
    background:linear-gradient(90deg,#2f6fed,#12a36a);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
    color:transparent;
}

#ROOT_ID .subtitle {
    text-align:center;
    font-size:clamp(13px,1.6vw,17px);
    margin:0 0 18px;
    opacity:0.8;
}

#ROOT_ID button {
    color:white;
    padding:10px clamp(12px,2vw,22px);
    border:0;
    border-radius:10px;
    cursor:pointer;
    font-size:clamp(13px,1.5vw,15px);
    font-weight:bold;
    white-space:nowrap;
    touch-action:manipulation;
    box-shadow:0 4px 10px rgba(0,0,0,0.22);
    transition:transform .12s, box-shadow .12s, filter .12s;
}
#ROOT_ID button:hover { transform:translateY(-1px); filter:brightness(1.08); }
#ROOT_ID button:active { transform:scale(0.97); }

#ROOT_ID .play  {background:linear-gradient(135deg,#27b57a,#168553);}
#ROOT_ID .pause {background:linear-gradient(135deg,#f0b429,#cf8a00);}
#ROOT_ID .reset {background:linear-gradient(135deg,#6b7488,#454c5e);}
#ROOT_ID .theme {
    background:linear-gradient(135deg,#8b6cff,#5a3fd4);
    position:absolute;
    top:clamp(24px,3vw,36px);
    right:clamp(8px,1.5vw,16px);
    padding:8px 14px;
    font-size:clamp(12px,1.3vw,14px);
    z-index:2;
}

/* ---------- two-column layout ---------- */
#ROOT_ID .layout {
    display:grid;
    grid-template-columns:310px minmax(0,1fr);
    gap:18px;
    align-items:start;
}

#ROOT_ID .panel {
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
    padding:14px;
}

#ROOT_ID .left { display:flex; flex-direction:column; gap:14px; }

#ROOT_ID .sigcard.x { --c:#2f6fed; }
#ROOT_ID .sigcard.h { --c:#f08a24; }

#ROOT_ID .sigcard h3 {
    margin:0 0 10px;
    font-size:17px;
    color:var(--c);
}

#ROOT_ID .tiles {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

#ROOT_ID .tile {
    cursor:pointer;
    border:2px solid #d3dcf0;
    border-radius:10px;
    padding:6px 4px 5px;
    text-align:center;
    font-size:12px;
    font-weight:bold;
    background:#ffffff;
    user-select:none;
    transition:border-color .12s, box-shadow .12s;
}
#ROOT_ID .tile:hover { border-color:var(--c); }
#ROOT_ID .tile.active {
    border-color:var(--c);
    box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 25%, transparent);
}
#ROOT_ID .tile svg { display:block; width:100%; height:34px; stroke:var(--c); }

#ROOT_ID .param {
    display:none;
    margin-top:10px;
    font-size:13px;
    font-weight:bold;
}
#ROOT_ID .param.show { display:block; }
#ROOT_ID .param input {
    display:block;
    width:100%;
    margin-top:5px;
    padding:7px;
    font-size:15px;
    border:1px solid #b9c5e0;
    border-radius:8px;
    background:#ffffff;
    color:#1f2a44;
    text-align:center;
}
#ROOT_ID .param input:focus {
    outline:none;
    border-color:var(--c);
    box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 25%, transparent);
}

#ROOT_ID .howto { font-size:13px; line-height:1.55; }
#ROOT_ID .howto b { color:#2f6fed; }
#ROOT_ID .howto ol { margin:6px 0 0; padding-left:20px; }

/* ---------- right column ---------- */
#ROOT_ID .right { min-width:0; }

#ROOT_ID .controls {
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:10px;
    margin-bottom:10px;
}

#ROOT_ID .controls .grow { flex:1 1 220px; min-width:160px; }
#ROOT_ID .controls input[type=range] { width:100%; accent-color:#2f6fed; }

#ROOT_ID .controls select {
    padding:8px;
    font-size:14px;
    font-weight:bold;
    border:1px solid #b9c5e0;
    border-radius:8px;
    background:#ffffff;
    color:#1f2a44;
}

#ROOT_ID .status {
    text-align:center;
    width:fit-content;
    max-width:100%;
    margin:0 auto 12px;
    padding:9px 20px;
    border-radius:999px;
    background:#ffffff;
    border:1px solid #d3dcf0;
    box-shadow:0 3px 10px rgba(31,42,68,0.08);
    font-size:clamp(12px,1.5vw,16px);
    font-weight:bold;
}

#ROOT_ID .plots { display:flex; flex-direction:column; gap:12px; min-width:0; }

#ROOT_ID canvas {
    display:block;
    max-width:100%;
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
}

/* ---------- dark mode ---------- */
#ROOT_ID.dark {
    background:linear-gradient(160deg,#0d1117 0%,#161d2e 100%);
    color:#e6edf7;
    box-shadow:0 10px 30px rgba(0,0,0,0.45);
}
#ROOT_ID.dark h2 {
    background:linear-gradient(90deg,#6aa9ff,#3ddc97);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
}
#ROOT_ID.dark .panel,
#ROOT_ID.dark canvas {
    background:linear-gradient(180deg,#1b2336,#111724);
    border-color:#2f3b57;
    box-shadow:0 6px 18px rgba(0,0,0,0.5);
}
#ROOT_ID.dark .sigcard.x { --c:#58a6ff; }
#ROOT_ID.dark .sigcard.h { --c:#ffb454; }
#ROOT_ID.dark .tile { background:#0f1522; border-color:#33415f; }
#ROOT_ID.dark .tile:hover,
#ROOT_ID.dark .tile.active { border-color:var(--c); }
#ROOT_ID.dark .param input,
#ROOT_ID.dark .controls select {
    background:#0f1522;
    color:#e6edf7;
    border-color:#3b4866;
}
#ROOT_ID.dark .status {
    background:#1a2233;
    border-color:#33415f;
    color:#e6edf7;
    box-shadow:0 3px 12px rgba(0,0,0,0.4);
}
#ROOT_ID.dark .howto b { color:#6aa9ff; }

/* ---------- responsive ---------- */
@media (max-width:900px) {
    #ROOT_ID .layout { grid-template-columns:1fr; }
    #ROOT_ID .left { flex-direction:row; flex-wrap:wrap; }
    #ROOT_ID .left .panel { flex:1 1 260px; }
}

@media (max-width:550px) {
    #ROOT_ID { padding:6px; }
    #ROOT_ID h2 { margin-top:64px; }
    #ROOT_ID .theme { padding:7px 11px; }
}
</style>

<button class="theme" id="theme">🌙 DARK MODE</button>

<h2>Convolution Integral of Continuous-Time Signals</h2>
<div class="subtitle">y(t) = ∫ x(τ) · h(t − τ) dτ</div>

<div class="layout">

    <!-- LEFT COLUMN: SIGNAL CHOICES -->
    <div class="left">
        <div class="panel sigcard x" id="card_x"></div>
        <div class="panel sigcard h" id="card_h"></div>

        <div class="panel howto">
            <b>How to read the plots</b>
            <ol>
                <li><b>Flip</b> h(τ) to get h(−τ).</li>
                <li><b>Shift</b> it by t to get h(t−τ).</li>
                <li><b>Multiply</b> it with x(τ).</li>
                <li><b>Integrate</b>: the shaded area is y(t).</li>
            </ol>
        </div>
    </div>

    <!-- RIGHT COLUMN: PLOTS -->
    <div class="right">

        <div class="controls">
            <button class="play" id="play">▶ PLAY</button>
            <button class="pause" id="pause">Ⅱ PAUSE</button>
            <button class="reset" id="reset">↺ RESET</button>

            <select id="speed" title="Animation speed">
                <option value="0.5">0.5× speed</option>
                <option value="1" selected>1× speed</option>
                <option value="2">2× speed</option>
                <option value="4">4× speed</option>
            </select>

            <div class="grow">
                <input id="tslider" type="range" min="-4" max="10" step="0.01" value="-4">
            </div>
        </div>

        <div class="status" id="status"></div>

        <div class="plots" id="plots">
            <canvas id="cTop"></canvas>
            <canvas id="cMid"></canvas>
            <canvas id="cBot"></canvas>
        </div>
    </div>

</div>

<script>
(function(){

const root=document.getElementById("ROOT_ID");
const $=s=>root.querySelector(s);

// ======================================
// SETTINGS
// ======================================

const TMIN=-8, TMAX=20;       // visible range for tau and t
const D=0.01;                 // tau resolution
const K=2;                    // result curve is sampled every K*D seconds
const N=Math.round((TMAX-TMIN)/D)+1;

const tau=new Float64Array(N);
for(let i=0;i<N;i++) tau[i]=TMIN+i*D;

const xArr=new Float64Array(N);   // x(tau)
const hCur=new Float64Array(N);   // h(t-tau) for the current t
const pCur=new Float64Array(N);   // x(tau)*h(t-tau) for the current t

let yArr=new Float64Array(0);     // full result y(t) on a time grid
let tGrid=new Float64Array(0);
let gX=1, gH=1, gP=1, gY=1;       // global maxima (fixed axis scales)

let time=TMIN;
let playing=false;
let lastTs=null;
let rafID=null;
let xf=null, hf=null;

// ======================================
// SIGNALS
// ======================================

const TYPES=[
    {id:"step",  label:"Unit step",        path:"M2 19 H18 V5 H38"},
    {id:"pulse", label:"Rect. pulse",      path:"M2 19 H10 V5 H26 V19 H38"},
    {id:"exp",   label:"Decaying exp.",    path:"M2 19 H10 V5 C14 15 22 18 38 19"},
    {id:"ramp",  label:"Ramp",             path:"M2 19 H12 L34 5"}
];

const sig={
    x:{type:"pulse", w:2, a:1},
    h:{type:"exp",   w:2, a:1}
};

function makeFn(s){
    if(s.type==="step")  return t=>t>=0?1:0;
    if(s.type==="pulse") return t=>(t>=0&&t<s.w)?1:0;
    if(s.type==="exp")   return t=>t>=0?Math.exp(-s.a*t):0;
    return t=>t>=0?0.2t:0;     // ramp
}

// ======================================
// LEFT COLUMN: BUILD THE SIGNAL CARDS
// ======================================

function buildCard(key){

    const card=$("#card_"+key);
    const title=key==="x"?"x(t)":"h(t)";

    let h='<h3>'+title+'</h3><div class="tiles">';

    TYPES.forEach(t=>{
        h+='<div class="tile" data-type="'+t.id+'">'+
           '<svg viewBox="0 0 40 24"><path d="'+t.path+
           '" fill="none" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'+
           t.label+'</div>';
    });

    h+='</div>';

    h+='<label class="param" data-for="pulse">Pulse width (s)'+
       '<input type="number" data-p="w" min="0.2" max="6" step="0.1" value="'+sig[key].w+'"></label>';

    h+='<label class="param" data-for="exp">Decay rate a  (e<sup>−at</sup>)'+
       '<input type="number" data-p="a" min="0.1" max="5" step="0.1" value="'+sig[key].a+'"></label>';

    card.innerHTML=h;

    card.querySelectorAll(".tile").forEach(el=>{
        el.addEventListener("click",()=>{
            sig[key].type=el.dataset.type;
            refreshCard(key);
            update();
        });
    });

    card.querySelectorAll(".param input").forEach(inp=>{
        inp.addEventListener("change",()=>{

            const p=inp.dataset.p;
            let v=Number(inp.value);

            const lo=Number(inp.min), hi=Number(inp.max);
            if(!Number.isFinite(v)) v=sig[key][p];
            v=Math.min(hi,Math.max(lo,v));

            inp.value=v;
            sig[key][p]=v;
            update();
        });
    });

    refreshCard(key);
}

function refreshCard(key){

    const card=$("#card_"+key);

    card.querySelectorAll(".tile").forEach(el=>{
        el.classList.toggle("active",el.dataset.type===sig[key].type);
    });

    card.querySelectorAll(".param").forEach(el=>{
        el.classList.toggle("show",el.dataset.for===sig[key].type);
    });
}

buildCard("x");
buildCard("h");

// ======================================
// THEMES
// ======================================

const themes={
    light:{text:"#1f2a44",tick:"#44506e",axis:"#44506e",zero:"#9aa6bf",grid:"#e0e6f3",
           x:"#2f6fed",h:"#f08a24",p:"#12a36a",y:"#8b5cf6",
           shade:"rgba(18,163,106,0.32)",ring:"#ffffff",
           legendBg:"rgba(255,255,255,0.92)",glow:4,future:0.2},
    dark:{text:"#e6edf7",tick:"#b4c0d9",axis:"#b4c0d9",zero:"#6e7b96",grid:"#27324a",
          x:"#58a6ff",h:"#ffb454",p:"#3ddc97",y:"#b794ff",
          shade:"rgba(61,220,151,0.36)",ring:"#111724",
          legendBg:"rgba(15,21,34,0.92)",glow:14,future:0.22}
};

let darkMode=!!(window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches);
let C=themes.light;
const themeBtn=$("#theme");

function applyTheme(){
    C=darkMode?themes.dark:themes.light;
    root.classList.toggle("dark",darkMode);
    themeBtn.textContent=darkMode?"☀ LIGHT MODE":"🌙 DARK MODE";
}

themeBtn.addEventListener("click",()=>{
    darkMode=!darkMode;
    applyTheme();
    render();
});

applyTheme();

// ======================================
// NUMERICS
// ======================================

function recompute(){

    xf=makeFn(sig.x);
    hf=makeFn(sig.h);

    let mx=0;
    for(let i=0;i<N;i++){
        xArr[i]=xf(tau[i]);
        if(xArr[i]>mx) mx=xArr[i];
    }

    let mh=0;
    for(let s=0;s<=TMAX-TMIN;s+=0.05){
        const v=hf(s);
        if(v>mh) mh=v;
    }

    gX=mx||1;
    gH=mh||1;

    // Full result y(t) = integral of x(tau) h(t-tau) d tau
    const M=Math.floor((N-1)/K)+1;
    yArr=new Float64Array(M);
    tGrid=new Float64Array(M);

    let pm=0, ym=0;

    for(let j=0;j<M;j++){

        const t=TMIN+j*K*D;
        tGrid[j]=t;

        let sum=0;

        for(let i=0;i<N;i++){

            const xv=xArr[i];
            if(xv===0) continue;

            const pv=xv*hf(t-tau[i]);
            sum+=pv;
            if(pv>pm) pm=pv;
        }

        yArr[j]=sum*D;
        if(yArr[j]>ym) ym=yArr[j];
    }

    gP=pm>1e-9?pm:1;
    gY=ym>1e-9?ym:1;
}

// h(t-tau), the product, and the area for one value of t
function computeAt(t){

    let sum=0;

    for(let i=0;i<N;i++){
        const hv=hf(t-tau[i]);
        hCur[i]=hv;
        pCur[i]=xArr[i]*hv;
        sum+=pCur[i];
    }

    return sum*D;
}

// ======================================
// CANVAS HELPERS
// ======================================

const plotsBox=$("#plots");
const cTop=$("#cTop"), cMid=$("#cMid"), cBot=$("#cBot");
const dpr=()=>window.devicePixelRatio||1;

function fit(){

    const w=Math.max(280,Math.floor(plotsBox.clientWidth));

    [[cTop,250],[cMid,250],[cBot,290]].forEach(([cv,h])=>{
        cv._w=w;
        cv._h=h;
        cv.style.width=w+"px";
        cv.style.height=h+"px";
        cv.width=Math.round(w*dpr());
        cv.height=Math.round(h*dpr());
    });
}

function begin(cv){
    const ctx=cv.getContext("2d");
    ctx.setTransform(dpr(),0,0,dpr(),0,0);
    ctx.clearRect(0,0,cv._w,cv._h);
    ctx.lineJoin="round";
    return ctx;
}

function makeArea(cv,ymin,ymax){

    const W=cv._w, H=cv._h;
    const L=60, R=W-22, T=36, B=H-44;

    return {
        W,H,L,R,T,B,ymin,ymax,
        X:v=>L+(v-TMIN)/(TMAX-TMIN)*(R-L),
        Y:v=>B-(v-ymin)/(ymax-ymin)*(B-T)
    };
}

function niceTicks(a,b,n){

    const raw=(b-a)/n;
    const mag=Math.pow(10,Math.floor(Math.log10(raw)));
    const r=raw/mag;
    const step=(r<=1?1:r<=2?2:r<=5?5:10)*mag;

    const ticks=[];
    for(let v=Math.ceil(a/step-1e-9)*step; v<=b+1e-9; v+=step){
        ticks.push(Math.abs(v)<1e-9?0:v);
    }

    return {ticks,step};
}

function fmt(v,step){
    const dec=Math.max(0,-Math.floor(Math.log10(step)+1e-9));
    return v.toFixed(dec);
}

function drawAxes(ctx,P,title,xlabel){

    const xt=niceTicks(TMIN,TMAX,Math.max(5,Math.floor((P.R-P.L)/70)));
    const yt=niceTicks(P.ymin,P.ymax,4);

    ctx.font="11px Arial";
    ctx.lineWidth=1;

    xt.ticks.forEach(v=>{
        const x=P.X(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(x,P.T); ctx.lineTo(x,P.B); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="center";
        ctx.fillText(fmt(v,xt.step),x,P.B+16);
    });

    yt.ticks.forEach(v=>{
        if(v<P.ymin-1e-9) return;
        const y=P.Y(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(P.L,y); ctx.lineTo(P.R,y); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="right";
        ctx.fillText(fmt(v,yt.step),P.L-8,y+4);
    });

    // zero lines
    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.5;
    ctx.beginPath();
    ctx.moveTo(P.L,P.Y(0)); ctx.lineTo(P.R,P.Y(0));
    ctx.moveTo(P.X(0),P.T); ctx.lineTo(P.X(0),P.B);
    ctx.stroke();

    // frame
    ctx.strokeStyle=C.axis;
    ctx.beginPath();
    ctx.moveTo(P.L,P.T); ctx.lineTo(P.L,P.B); ctx.lineTo(P.R,P.B);
    ctx.stroke();

    ctx.fillStyle=C.text;
    ctx.textAlign="left";
    ctx.font="bold 14px Arial";
    ctx.fillText(title,P.L,22);

    ctx.textAlign="center";
    ctx.font="13px Arial";
    ctx.fillText(xlabel,(P.L+P.R)/2,P.H-8);
}

function roundRect(ctx,x,y,w,h,r){
    ctx.beginPath();
    ctx.moveTo(x+r,y);
    ctx.arcTo(x+w,y,x+w,y+h,r);
    ctx.arcTo(x+w,y+h,x,y+h,r);
    ctx.arcTo(x,y+h,x,y,r);
    ctx.arcTo(x,y,x+w,y,r);
    ctx.closePath();
}

// items: [{color, label, fill}]
function drawLegend(ctx,P,items){

    ctx.font="bold 12px Arial";

    let w=0;
    items.forEach(it=>{ w=Math.max(w,ctx.measureText(it.label).width); });
    w+=44;

    const h=10+items.length*20;
    const x=P.R-w-8;
    const y=P.T+8;

    roundRect(ctx,x,y,w,h,8);
    ctx.fillStyle=C.legendBg;
    ctx.fill();

    items.forEach((it,k)=>{

        const yy=y+20+k*20;

        if(it.fill){
            ctx.fillStyle=it.fill;
            ctx.fillRect(x+10,yy-9,22,10);
        }
        else{
            ctx.strokeStyle=it.color;
            ctx.lineWidth=3;
            ctx.beginPath(); ctx.moveTo(x+10,yy-4); ctx.lineTo(x+32,yy-4); ctx.stroke();
        }

        ctx.fillStyle=it.color;
        ctx.textAlign="left";
        ctx.fillText(it.label,x+38,yy);
    });
}

function trace(ctx,P,arr){
    ctx.beginPath();
    for(let i=0;i<N;i++){
        const x=P.X(tau[i]), y=P.Y(arr[i]);
        if(i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
    }
}

function clipTo(ctx,P){
    ctx.save();
    ctx.beginPath();
    ctx.rect(P.L,P.T,P.R-P.L,P.B-P.T);
    ctx.clip();
}

function vline(ctx,P,x,color,alpha){
    ctx.save();
    ctx.globalAlpha=alpha;
    ctx.strokeStyle=color;
    ctx.lineWidth=1.6;
    ctx.setLineDash([5,5]);
    ctx.beginPath(); ctx.moveTo(x,P.T); ctx.lineTo(x,P.B); ctx.stroke();
    ctx.restore();
}

// ======================================
// PLOT 1: x(tau) AND h(t-tau)
// ======================================

function drawTop(t){

    const ctx=begin(cTop);

    // Very large values (e.g. ramps) are clipped to keep unit signals readable
    const s0=Math.max(1.2,Math.min(Math.max(gX,gH),6))*1.12;
    const P=makeArea(cTop,-0.12*s0,s0);

    drawAxes(ctx,P,"① x(τ)  and  h(t − τ)","τ  (dummy variable)");

    clipTo(ctx,P);

    vline(ctx,P,P.X(t),C.h,0.7);

    ctx.strokeStyle=C.x;
    ctx.lineWidth=3;
    trace(ctx,P,xArr);
    ctx.stroke();

    ctx.save();
    ctx.shadowColor=C.h;
    ctx.shadowBlur=C.glow;
    ctx.strokeStyle=C.h;
    ctx.lineWidth=3;
    trace(ctx,P,hCur);
    ctx.stroke();
    ctx.restore();

    ctx.restore();

    // marker at tau = t
    const mx=P.X(t);
    ctx.fillStyle=C.h;
    ctx.beginPath();
    ctx.moveTo(mx,P.B-9); ctx.lineTo(mx-6,P.B); ctx.lineTo(mx+6,P.B);
    ctx.closePath();
    ctx.fill();

    drawLegend(ctx,P,[
        {color:C.x,label:"x(τ)"},
        {color:C.h,label:"h(t − τ),  t = "+t.toFixed(2)}
    ]);
}

// ======================================
// PLOT 2: PRODUCT AND SHADED AREA
// ======================================

function drawMid(t,area){

    const ctx=begin(cMid);

    const top=gP*1.18;
    const P=makeArea(cMid,-0.12*top,top);

    drawAxes(ctx,P,"② x(τ) · h(t − τ)   (shaded area = y(t))","τ  (dummy variable)");

    clipTo(ctx,P);

    // faint reference outlines of the two signals
    ctx.save();
    ctx.globalAlpha=0.35;
    ctx.lineWidth=1.6;

    ctx.strokeStyle=C.x;
    trace(ctx,P,xArr);
    ctx.stroke();

    ctx.strokeStyle=C.h;
    trace(ctx,P,hCur);
    ctx.stroke();

    ctx.restore();

    vline(ctx,P,P.X(t),C.h,0.6);

    // shaded area under the product
    ctx.beginPath();
    ctx.moveTo(P.X(tau[0]),P.Y(0));
    for(let i=0;i<N;i++) ctx.lineTo(P.X(tau[i]),P.Y(pCur[i]));
    ctx.lineTo(P.X(tau[N-1]),P.Y(0));
    ctx.closePath();
    ctx.fillStyle=C.shade;
    ctx.fill();

    // product curve
    ctx.save();
    ctx.shadowColor=C.p;
    ctx.shadowBlur=C.glow;
    ctx.strokeStyle=C.p;
    ctx.lineWidth=2.8;
    trace(ctx,P,pCur);
    ctx.stroke();
    ctx.restore();

    ctx.restore();

    drawLegend(ctx,P,[
        {color:C.p,label:"x(τ) · h(t − τ)"},
        {color:C.p,label:"Area = "+area.toFixed(3),fill:C.shade}
    ]);
}

// ======================================
// PLOT 3: RESULT y(t)
// ======================================

function drawBot(t,area){

    const ctx=begin(cBot);

    const top=gY*1.18;
    const P=makeArea(cBot,-0.1*top,top);

    drawAxes(ctx,P,"③ y(t) = x(t) ∗ h(t)","t  (seconds)");

    clipTo(ctx,P);

    const px=P.X(t), py=P.Y(area);

    vline(ctx,P,px,C.y,0.45);

    // future: very light
    ctx.save();
    ctx.globalAlpha=C.future;
    ctx.strokeStyle=C.y;
    ctx.lineWidth=3;
    ctx.beginPath();
    ctx.moveTo(px,py);
    for(let j=0;j<tGrid.length;j++){
        if(tGrid[j]>t) ctx.lineTo(P.X(tGrid[j]),P.Y(yArr[j]));
    }
    ctx.stroke();
    ctx.restore();

    // past: solid
    ctx.save();
    ctx.shadowColor=C.y;
    ctx.shadowBlur=C.glow;
    ctx.strokeStyle=C.y;
    ctx.lineWidth=3.2;
    ctx.beginPath();
    let started=false;
    for(let j=0;j<tGrid.length;j++){
        if(tGrid[j]<=t){
            const x=P.X(tGrid[j]), y=P.Y(yArr[j]);
            if(!started){ ctx.moveTo(x,y); started=true; } else ctx.lineTo(x,y);
        }
    }
    if(!started) ctx.moveTo(px,py);
    ctx.lineTo(px,py);
    ctx.stroke();
    ctx.restore();

    ctx.restore();

    // current point
    ctx.save();
    ctx.shadowColor=C.y;
    ctx.shadowBlur=C.glow+4;
    ctx.fillStyle=C.y;
    ctx.beginPath(); ctx.arc(px,py,8,0,2*Math.PI); ctx.fill();
    ctx.restore();

    ctx.strokeStyle=C.ring;
    ctx.lineWidth=2.5;
    ctx.beginPath(); ctx.arc(px,py,8,0,2*Math.PI); ctx.stroke();

    drawLegend(ctx,P,[
        {color:C.y,label:"y(t) = "+area.toFixed(3)}
    ]);
}

// ======================================
// RENDER
// ======================================

function render(){

    const area=computeAt(time);

    drawTop(time);
    drawMid(time,area);
    drawBot(time,area);

    $("#status").textContent=
        "t = "+time.toFixed(2)+" s   |   y(t) = ∫ x(τ) h(t−τ) dτ = "+area.toFixed(3);

    $("#tslider").value=time;
}

function update(){
    recompute();
    render();
}

// ======================================
// ANIMATION
// ======================================

const BASE_SPEED=2;   // seconds of signal time per real second

function animate(ts){

    if(!playing) return;

    if(lastTs!==null){
        const dt=Math.min((ts-lastTs)/1000,0.05);
        time+=dt*BASE_SPEED*Number($("#speed").value);
    }

    lastTs=ts;

    if(time>=TMAX){
        time=TMAX;
        render();
        pause();
        return;
    }

    render();
    rafID=requestAnimationFrame(animate);
}

function pause(){
    playing=false;
    if(rafID!==null) cancelAnimationFrame(rafID);
    rafID=null;
    lastTs=null;
}

$("#play").addEventListener("click",()=>{

    if(playing) return;
    if(time>=TMAX) time=TMIN;

    playing=true;
    lastTs=null;
    rafID=requestAnimationFrame(animate);
});

$("#pause").addEventListener("click",pause);

$("#reset").addEventListener("click",()=>{
    pause();
    time=TMIN;
    render();
});

$("#tslider").addEventListener("input",e=>{
    pause();
    time=Number(e.target.value);
    render();
});

// ======================================
// RESPONSIVE RESIZING
// ======================================

function resize(){
    fit();
    render();
}

if(typeof ResizeObserver!=="undefined"){
    new ResizeObserver(resize).observe(plotsBox);
}
window.addEventListener("resize",resize);

// initial display
fit();
update();

})();
</script>

</div>
"""

html = html.replace("ROOT_ID", uid)

# Everything runs in the browser (JavaScript), so play/pause/slider stay smooth
# and never trigger Streamlit reruns.
components.html(html, height=1250, scrolling=True)
