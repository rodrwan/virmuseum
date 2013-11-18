class RecommendsController < ApplicationController
  # GET /recommends
  # GET /recommends.json
  def index
    @tvis = TermVsItem.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @tvis }
    end
  end

  # GET /recommends/1
  # GET /recommendss/1.json
  before_filter :get_connection
  def show
    # @tvi = TermVsItem.find(params[:id])
    user = Rack::Utils.escape(params[:user])
    @item = Item.find((params[:item_id].to_i+1))
    name = @item.name
    hierarchy = @item.hierarchy.name
    item = { :item_id => params[:item_id], :user => user }
    response = @conn.get_recommend(item)
    response = response.body
    response = JSON.parse(response)
    if response['elements'] > 0
      respond_to do |format|
        response['recommended_for'] = name
        response['hierarchy'] = hierarchy
        format.json {render json: response }
      end
    else
      respond_to do |format|
        format.json {render json: response }
      end
    end
    # respond_to do |format|
    #   format.html # show.html.erb
    #   format.json { render json: @item }
    # end
  end

  def get_connection
    @conn = Connection.new
  end
end
