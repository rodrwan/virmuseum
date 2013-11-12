class Connection
  attr_accessor :conn

  def initialize(options={})
    require 'faraday'
    url =options[:url] || VIRMUSEUM_API_URL
    @conn = Faraday.new(:url => url) do |req|
      req.request :url_encoded
      req.response :logger
      req.adapter Faraday.default_adapter
      req.options[:timeout] = 5
      req.options[:open_timeout] = 3
    end
  end

  def get_recommend(item)
    puts item[:item_id] + " " + item[:user]
    conn.post '/recommend/get', { :item_id => item[:item_id].to_i, :user => item[:user] }
  end
end