const http=require('node:http'), fs=require('node:fs'), path=require('node:path');
const {chromium}=require('playwright');const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const server=http.createServer((req,res)=>{let file;try{file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));}catch{res.writeHead(400);return res.end();}if(!file.startsWith(root+path.sep)&&file!==root){res.writeHead(403);return res.end();}if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');if(!fs.existsSync(file)){res.writeHead(404);return res.end();}res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'application/javascript; charset=utf-8','.css':'text/css; charset=utf-8'})[path.extname(file)]||'application/octet-stream');fs.createReadStream(file).pipe(res);});
(async()=>{let browser;try{await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));browser=await chromium.launch();const context=await browser.newContext({viewport:{width:1440,height:1080},reducedMotion:'reduce'});const p=await context.newPage();p.setDefaultTimeout(15000);const errors=[];p.on('pageerror',e=>errors.push(e.message));

await p.goto('http://127.0.0.1:'+server.address().port+'/',{waitUntil:'domcontentloaded'});

   assert.match(await p.locator('#status').innerText(),/1461/);await p.locator('#start').fill('2024-02-01');await p.locator('#end').fill('2024-02-29');assert.match(await p.locator('#status').innerText(),/29 daily/);
   await p.locator('#metric').selectOption('CO');assert.match(await p.locator('#trendTitle').innerText(),/CO/);await p.locator('#threshold').fill('500');assert.match(await p.locator('#exceedance').innerText(),/^0 days/);
   const dl=p.waitForEvent('download');await p.locator('#summary').click();assert.equal((await dl).suggestedFilename(),'delhi-research-summary.md');
   await p.locator('#start').fill('2024-12-01');assert.match(await p.locator('#status').innerText(),/Start date is after/);await p.locator('#reset').click();
assert.deepEqual(errors,[],'Unexpected page errors');await p.setViewportSize({width:390,height:844});await p.waitForTimeout(200);assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2),false,'Mobile horizontal overflow');console.log('V2 workflow, exports, reload behavior and mobile checks passed.');
}finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}})().catch(e=>{console.error(e);process.exitCode=1;});
