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
  def show
    @tvi = TermVsItem.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @item }
    end
  end
end
