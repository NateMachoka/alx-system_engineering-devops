#!/usr/bin/env ruby

puts ARGV[0].scan(/hbt+n/).reject { |match| match == "hbon" }.join
