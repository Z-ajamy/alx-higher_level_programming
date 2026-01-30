#!/usr/bin/env node

args = process.argv.slice(2);
if(args.length === 0) console.log("No argument");
if(args.length === 1) console.log("Argument found");
if(args.length === 2) console.log("Arguments found");

